from pymongo import MongoClient

URL = "mongodb://top-theme-mongo:L4SDrxH8M7jk9Z7iotMcx6FxOPLaF6CWkF2ZfUhQKiAK5zN3KqFkQFNVLCsyGNTGapk0RGLZD1YiIuVLQRoC5w==@top-theme-mongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
DB_NAME = "test"

conn = MongoClient(URL)
db = conn[DB_NAME]

lst_colletion = ["corpus", "queries", "themes", "cluster_analysis"]

def insert(collection_name, data):
    if not check_collection_name(collection_name):
        return 0;
    collection = db[collection_name]

    if isinstance(data, list):
        collection.insert_many(data)
    if isinstance(data, dict):
        collection.insert_one(data)


def update(collection_name, old_data, new_data):
    if not check_collection_name(collection_name):
        return 0;
    collection = db[collection_name]
    collection.update(old_data,new_data)


def find_documents(collection_name, dict_criteria):
    if not check_collection_name(collection_name):
        return 0;
    collection = db[collection_name]

    documents = collection.find(dict_criteria)
    return documents


def find_all(collection_name):
    if not check_collection_name(collection_name):
        return 0;
    collection = db[collection_name]
    return collection.find()


def count_documents_within_collection(collection_name):
    if not check_collection_name(collection_name):
        return 0;
    collection = db[collection_name]
    return collection.count_documents()


def check_collection_name(collection_name):
    if collection_name not in lst_colletion:
        print("[ERROR] The collection is not existed.")
        return False
    else:
        return True
