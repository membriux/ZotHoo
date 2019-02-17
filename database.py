

import pymongo


# Database global variables/initializers
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ICSdatabase']


def test_db_connection():
    print('DB: Databases:', client.list_database_names())
    print('DB: testing connection')
    url_cols = db['URLs']
    for col_item in url_cols.find():
        print(col_item)


if __name__ == '__main__':
    client.drop_database(db)
    test_db_connection()



