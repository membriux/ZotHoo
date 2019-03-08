import os
import pymongo
from tqdm import tqdm

from collections import OrderedDict
from src.tokenizer import Tokenizer
from src.indexer import read_directory
from src.parser import parse
import config
import pprint
import json

Index = dict()
Header = dict()

pp = pprint.PrettyPrinter()

def build_index():
    global Index, Header
    tokenizer = Tokenizer()
    for subdir in os.listdir(config.RAW_WEBPAGES):
        full_subdir = os.path.join(config.RAW_WEBPAGES, subdir)
        if os.path.isdir(full_subdir):
            to_parse = read_directory(full_subdir)
            print("Subdirectory: ", subdir)
            for _file in tqdm(to_parse):
                filename = "/".join(_file.split("/")[1:])
                header, txt = parse(_file)

                Header[filename] = header
                token_counter = tokenizer.counter_tokenize(txt)
                for tok in token_counter:
                    if tok not in Index:
                        Index[tok] = { filename : token_counter[tok]}
                    else:
                        Index[tok][filename] = token_counter[tok]
    save_index()
    save_header()

def save_header():
    with open(config.HEADER_PATH, 'w') as f:
        json.dump(Header, f, sort_keys=True, indent=4)
    print("[Saved Header succesfully on {}]".format(config.HEADER_PATH))                

def save_index():
    with open(config.INDEX_PATH, 'w') as f:
        json.dump(Index, f, sort_keys=True, indent=4)
    print("[Saved Index succesfully on {}]".format(config.INDEX_PATH))




def main():
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    # client.drop_database("ICSdatabase")
    # db = client['ICSdatabase']
    build_index()

    # pp.pprint(Index)


if __name__ == '__main__':
    main()
