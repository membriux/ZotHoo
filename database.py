
import pymongo


# Database global variables/initializers
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ICSdatabase']


def test_db_connection():
    print('DB: testing connection')
    print('DB: adding URL col')
    print('DB: Databases:', client.list_database_names())
    print('DB: Successfully created col: URLs')
    url_cols = db['URLs']
    for col_item in url_cols.find():
        print(col_item)


if __name__ == '__main__':
    test_db_connection()



