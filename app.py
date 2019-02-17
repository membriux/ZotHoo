
import pymongo


def main():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    client.drop_database("ICSdatabase")
    db = client['ICSdatabase']







if __name__ == '__main__':
    main()


