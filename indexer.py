

import database
import os

FILES = []


def read_directory(directory):
    for item in directory:
        if os.path.isdir(os.path.join('.', item)):
            read_directory(item)
        else:
            print(item)


def main():
    sub_directories = os.listdir('WEBPAGES_RAW')
    # Assuming the main directory contains directories
    # and each directory contains files
    for item in sub_directories:
        if os.path.isdir(os.path.join(item)):
            print(item, 'isDir')
            read_directory(item)
        else:
            print(item, 'not a directory')


if __name__ == '__main__':
    main()







