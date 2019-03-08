from bs4 import BeautifulSoup
import requests
import lxml
import time

class Document:

    def __init__(self, url):
        self.url = url
        self.heading = self.get_heading()

    def get_heading(self):
        result = requests.get('http://' + self.url)
        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        header = ''
        if soup.find('h1') != None:
            return soup.find('h1').get_text()
        elif soup.find('title') != None and 'Facebook' in soup.find('title').get_text():
            return soup.find('title').get_text()
        elif soup.find('body') != None:
            s = soup.findChildren('body')[0].get_text()
            header = re.sub('\n|\t', '', s)
            return header[0:48]
        else:
            s = soup.get_text()
            header = re.sub('\n|\t', '', s)
            return header[0:48]
