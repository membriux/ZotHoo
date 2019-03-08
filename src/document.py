from bs4 import BeautifulSoup
import requests
import lxml
import time

class Document:

    def __init__(self, url, header):
        self.url = url
        self.heading = header

    
