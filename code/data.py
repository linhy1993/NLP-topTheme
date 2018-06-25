import os
import pickle
import json

IF_DEBUG = False

def save_pickle(data, file_path):
    if not file_path.endswith(".pickle"):
        print("[ERROR] file suffix missing or file suffix is not appropriate.")
    else:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)


def read_pickle(file_path):
    data = ""
    if not file_path.endswith(".pickle"):
        print("[ERROR] file suffix missing or file suffix is not appropriate.")
    else:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
    return data


def save_txt(str_data, file_path):
    if not file_path.endswith(".txt"):
        print("[ERROR] file suffix missing or file suffix is not appropriate.")
    else:
        with open(file_path, 'w') as file:
            file.write(str_data)


def read_txt(file_path):
    if IF_DEBUG:
        print("[INFO] read_txt from " + file_path)

    data = ""
    if not file_path.endswith(".txt"):
        print("[ERROR] file suffix missing or file suffix is not appropriate.")
    else:
        with open(file_path, 'r') as file:
            data = file.read()
    return data


def str_of(data):
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    """
    test function
    """
    # test read_txt
    print("----- test read_txt -----")
    test_data = read_txt('input/in0.txt')
    print(test_data)

    # test save_txt
    print("----- test save_txt -----")
    save_txt(test_data, 'data_test.txt')

    # test save_pickle & read_pickle
    print("----- test save_pickle & read_pickle -----")
    test_file = 'data_test_pickle.pickle'
    save_pickle(test_data, test_file)
    data = read_pickle(test_file)
    print(data)
