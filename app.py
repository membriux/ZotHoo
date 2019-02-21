
import os
import pymongo
from tqdm import tqdm

from collections import OrderedDict
from tokenizer import Tokenizer
from indexer import read_directory
from parser import parse
import config

Index = OrderedDict()

def build_index():
    global Index
    tokenizer = Tokenizer()
    for subdir in os.listdir(config.RAW_WEBPAGES):
        full_subdir = os.path.join(config.RAW_WEBPAGES, subdir)
        if os.path.isdir(full_subdir):
            to_parse = read_directory(full_subdir)
            print("Subdirectory: ", subdir)
            for _file in tqdm(to_parse):
                filename = "/".join(_file.split("/")[1:])
                parsed_txt = parse(_file)
                token_counter = tokenizer.counter_tokenize(parsed_txt)
                for tok in token_counter:
                    if tok not in Index:
                        Index[tok] = { filename : token_counter[tok]}
                    else:
                        Index[tok][filename] = token_counter[tok]

def main():
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    # client.drop_database("ICSdatabase")
    # db = client['ICSdatabase']
    build_index()
    for i, (key, value) in enumerate(Index.items()):
        print("[{}] {}\t{}".format(i, key, value))
        if i == 100:
            break
    

    



if __name__ == '__main__':
    main()


