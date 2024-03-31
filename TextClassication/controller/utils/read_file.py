import glob
import os

from TextClassication.model.TestData import TestData

base_directory = "Dataset/Classification-Train And Test/"
base_extension = "/*.txt"


def get_classes_names():
    return [os.path.basename(os.path.normpath(class_path)) for class_path in glob.glob(base_directory + "*")]


def get_classes_path():
    return glob.glob(base_directory + "*")


def get_classes_files_count():
    classes_probs = {}

    for class_prob in get_classes_path():
        classes_probs[os.path.basename(os.path.normpath(class_prob))] = len(glob.glob(class_prob+'/*.txt'))

    return classes_probs


def read_file(file_path: str):
    with open(file_path, "r") as file:
        data = file.read()

    return data


def read_files(key: str):
    text_files = glob.glob(key + "/*.txt")
    return ' '.join(map(read_file, text_files))


def read_test_data(key: str):
    text_files = glob.glob(key + "/test/*.txt")
    my_list = map(read_file, text_files)
    dic = {}
    for i in range(len(text_files)):
        dic[text_files[i]] = my_list[i]
    return dic


def read_classification_train_files():
    keys = get_classes_path()
    data = {}
    for key in keys:
        data[os.path.basename(os.path.normpath(key))] = read_files(key)

    return data


def create_label_value_dict(label, text_file):
    dic = {}
    data = read_file(text_file)
    dic[label] = data

    return dic


def read_classification_test_files_using_class():
    keys = get_classes_path()
    data = {}
    for key in keys:
        text_files = glob.glob(key + "/test/*.txt")
        for text_file in text_files:
            data[os.path.basename(os.path.normpath(text_file))] = TestData(os.path.basename(os.path.normpath(key)), read_file(text_file))
            # data[text_file] = create_label_value_dict(key, text_file)

    return data


def read_classification_test_files():
    keys = get_classes_path()
    data = {}
    for key in keys:
        text_files = glob.glob(key + "/test/*.txt")
        for text_file in text_files:
            data[os.path.basename(os.path.normpath(text_file))] = create_label_value_dict(os.path.basename(os.path.normpath(key)), text_file)

    return data
