

import config
import os
from bs4 import BeautifulSoup as bs
# use folder 2, file 55

"""
    Methods: counter, tokenizer

"""
invalid_files = []

invalid_tags = ['style', 'script', 'a', 'meta',
                'link', 'ul', 'li', 'table', 'td',
                'select', 'option', 'tr', 'form']

html_parser = 'html.parser'


def parse(_file) -> str:
    all_text = ''
    # Open file and read it using bs4
    try:
        with open(_file, 'r', encoding="utf-8") as f:
            soup = bs(f, html_parser)
            # Remove unnecessary text from file
            for i in invalid_tags:
                while soup.find(i) is not None:
                    soup.find(i).decompose()

            all_text += soup.get_text()
    except Exception as _:
        invalid_files.append(_file)
    
    return all_text


if __name__ == '__main__':
    file = config.RAW_WEBPAGES + '/2/55'
    print(parse(file))

