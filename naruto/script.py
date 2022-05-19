from bs4 import BeautifulSoup
import requests
from html.parser import HTMLParser
import time

#path to save images
savePath = "C:\\Users\\aleph\\Pictures\\naruto"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
  }

#verify image exist in the path
def image_exist(imgName):
    try:
        f = open(savePath + "\\{}.jpg".format(imgName))
        f.close()
        return True
    except:
        return False

#extract the img name from url
def get_img_name(url):
    url_split = url.split("/")
    imgName = url_split[len(url_split) - 1].split(".")[0]
    imgName = ''.join(char for char in imgName if char.isalnum())
    return imgName

#download the image file
def download_file(url, endereco):
    resposta = requests.get(url, headers=headers)

    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
    print("Downloaded, save in {}".format(endereco))
    time.sleep(5)

#get the url and format that to download
def format_url(url):
    urlFormated = "https://wallpaper-house.com/"
    urlFormated += url.replace("../../", "")
    return urlFormated

#function to parse html
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if(tag == "img" and attr[0] == "src"):
                url = format_url(attr[1])
                imgName = get_img_name(url)
                if(image_exist(imgName) == False):
                    download_file(url, savePath + "\\{}.jpg".format(imgName))
                else:
                    print("Imagem já existe no diretorio! Indo para a próxima!")
                


#init the requests
url = "https://wallpaper-house.com/group/best-naruto-wallpapers/index.php"
req = requests.get(url, headers=headers)
html = str(req.content)
parser = MyHTMLParser()
parser.feed(html)
