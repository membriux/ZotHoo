

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
    # Open file and read it using bs4
    try:
        with open(_file, 'r', encoding="utf-8") as f:
            soup = bs(f, html_parser)
            # Remove unnecessary text from file
            for tag in valid_tags:
                soup.find_all(tag)

            all_text += soup.get_text()
    except Exception as _:
        print('invalid')
        invalid_files.append(_file)
    
    return all_text


if __name__ == '__main__':
    file = config.RAW_WEBPAGES + '/2/10'
    print(parse(file))

