# import database
# import os

# FILES = []


# def read_directory(directory):
#     _files = []
#     for item in os.listdir(directory):
#         subitem = os.path.join(directory, item)
#         if os.path.isdir(subitem):
#             _files = _files + read_directory(subitem)
#         else:
#             _files.append(subitem)
#     return _files


# def main():
#     # Assuming the main directory contains directories
#     # and each directory contains files
#     for item in os.listdir(config.RAW_WEBPAGES):
#         subdir = os.path.join(config.RAW_WEBPAGES, item)
#         if os.path.isdir(subdir):
#             read_directory(subdir)



# if __name__ == '__main__':
#     main()
