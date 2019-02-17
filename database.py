

import pymongo


# Database global variables/initializers
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ICSdatabase']
token_col = db['Tokens']


def test_db_connection():
    print('DB: Databases:', client.list_database_names())
    print('DB: Testing connection...')
    print('DB: Database up and running')


def create_table():
    test_token = {'Token': 'Hello_world', 'Documents': [{'doc1': 4}] }
    token_col.insert_one(test_token)
    print('DB: Inserted test token:', token_col.find_one())


def save(token):
    if token not in token_col:
        token_col.insert_one(token)
    else:
        token = {"Token": token.key()}
        add_docs = {'$push': {'Documents': token.values()}}
        token_col.update(token, add_docs)
    print('DB: New token added... \n\n', token_col.find_one())


if __name__ == '__main__':
    client.drop_database(db)
    test_db_connection()
    create_table()
    new_token = {'Token': 'Hello_world', 'Documents': [{'doc5': 10}]}
    save(new_token)



