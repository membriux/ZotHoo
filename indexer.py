

import database
import os
import config

FILES = []


def read_directory(directory):
    for item in os.listdir(directory):
        subitem = os.path.join(directory, item)
        if os.path.isdir(subitem):
            read_directory(subitem)
        else:
            with open(subitem, 'r') as f:
                print(subitem)


def main():


    # Assuming the main directory contains directories
    # and each directory contains files
    for item in os.listdir(config.RAW_WEBPAGES):
        subdir = os.path.join(config.RAW_WEBPAGES, item)
        if os.path.isdir(subdir):
            read_directory(subdir)
            break
        else:
            print("*"*10,item)


if __name__ == '__main__':
    main()







