

import config
import os
from bs4 import BeautifulSoup as bs
# use folder 2, file 55

"""
    Methods: counter, tokenizer

"""
invalid_files = []

valid_tags = ['body', 'title', 'h1', 'h2', 'h3', 'strong', 'b']

html_parser = 'html.parser'


def parse(_file) -> str:
    all_text = ''
    header = ''
    # Open file and read it using bs4
    try:
        with open(_file, 'r', encoding="utf-8") as f:
            soup = bs(f, html_parser)
            # Get header

            header = get_header(soup)

            for tag in valid_tags:

                soup.find_all(tag)

            all_text += soup.get_text()
            all_text = remove_invalids(all_text)
    except Exception as _:
        print('invalid: ', _file)
        invalid_files.append(_file)

    return all_text

def get_header(soup):
        result = requests.get('http://' + self.url)
        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        if soup.find('h1') != None:
            return soup.find('h1').get_text()
        elif 'Facebook' in soup.title.get_text():
            return soup.title.get_text()
        else:
            return soup.findChildren('body')[0].get_text()[0:48] + '...'



def remove_invalids(string):
    return ''.join([c if ord(c) < 128 else ' ' for c in string])



if __name__ == '__main__':
    file = config.RAW_WEBPAGES + '/2/10'
    print(parse(file))
