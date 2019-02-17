
import os
import pymongo
from tqdm import tqdm

from tokenizer import Tokenizer
from indexer import read_directory
from parser import parse
import config

def main():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    client.drop_database("ICSdatabase")
    db = client['ICSdatabase']
    tokenizer = Tokenizer()

    for subdir in tqdm(os.listdir(config.RAW_WEBPAGES)):
        full_subdir = os.path.join(config.RAW_WEBPAGES, subdir)
        if os.path.isdir(full_subdir):
            to_parse = read_directory(full_subdir)

            for _file in to_parse:
                parsed_txt = parse(_file)
                token_counter = tokenizer.counter_tokenize(parsed_txt)
                for tok in token_counter:
                    



if __name__ == '__main__':
    main()


