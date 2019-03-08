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
        if soup.find('h1') != None:
            return soup.find('h1').get_text()
        elif 'Facebook' in soup.title.get_text():
            return soup.title.get_text()
        else:
            return soup.findChildren('body')[0].get_text()[0:48] + '...'



if __name__ == '__main__':
    # link = 'www.ics.uci.edu/facebook/login/browse/fanned_pages/search/str/%25E6%2595%2599%25E8%2582%25B2/keywords_pages/UCIBrenICS/photos/a.10150104180706909.283411.106291486908/10154351203306909?type=3'
    # d = Document(link)
    # print('URL:\n\n', d.url,'HEADING\n\n', d.heading)
