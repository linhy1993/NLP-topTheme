import os
import pickle
import json

def save_pickle(data, file_path):
    if not file_path.endswith(".pickle"):
        print("ERROR: file suffix missing or file suffix is not appropriate.")
        pass
    with open(file_path, 'wb') as file:
        pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)


def read_pickle(data, file_path):
    if not file_path.endswith(".pickle"):
        print("ERROR: file suffix missing or file suffix is not appropriate.")
        pass
    with open(file_path, 'rb') as file:
        data = pickle.load(file)


def save_txt(str_data, file_path):
    if not file_path.endswith(".txt"):
        print("ERROR: file suffix missing or file suffix is not appropriate.")
        pass
    with open(file_path, 'w') as file:
        file.write(str_data)


def read_txt(str_data, file_path):
    if not file_path.endswith(".txt"):
        print("ERROR: file suffix missing or file suffix is not appropriate.")
        pass
    with open(file_path, 'r') as file:
        str_data = file.read()


def str_of(data):
    return json.dumps(d, ensure_ascii=False)
