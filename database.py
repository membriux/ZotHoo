

import pymongo


# Database configuration variables/initializers
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ICSdatabase']
token_col = db['Tokens']


def test_db_connection():
    print('DB: Databases:', client.list_database_names())
    print('DB: Testing connection...')
    print('DB: Database OK')


def create_table():
    """
    To create a table, there must be a value inserted into it.
    """
    test_token = {'Token': 'Hello_world', 'Documents': [{'doc1': 4}]}
    token_col.insert_one(test_token)
    # print('DB: Inserted test token:', token_col.find_one())


def save(token):
    """
     Saves/update token in db.
    """
    t, docs = token['Token'], token['Documents']
    query_tok = {'Token': t}
    if not token_col.find(query_tok):
        token_col.insert_one(token)
    else:
        add_docs = {'$push': {'Documents': {'$each': docs}}}
        token_col.update_one(query_tok, add_docs)


if __name__ == '__main__':
    client.drop_database(db)
    test_db_connection()
    create_table()



