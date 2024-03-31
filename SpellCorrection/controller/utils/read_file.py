def read_from_file(filepath):
    with open(filepath, "r") as file:
        data = file.read()

    return data


def read_dataset_file():
    return read_from_file("Dataset/Spelling Dataset/test/Dictionary/Dataset.data")


def read_dictionary_file():
    return read_from_file("Dataset/Spelling Dataset/test/Dictionary/dictionary.data")


def read_spell_test_set_file():
    return read_from_file("Dataset/Spelling Dataset/test/spell-testset.txt")


def read_confusion_matrices_file():
    import ast
    return {
        "deletion": ast.literal_eval(
            read_from_file("Dataset/Spelling Dataset/test/Confusion Matrix/del-confusion.data")),
        "insertion": ast.literal_eval(
            read_from_file("Dataset/Spelling Dataset/test/Confusion Matrix/ins-confusion.data")),
        "substitution": ast.literal_eval(
            read_from_file("Dataset/Spelling Dataset/test/Confusion Matrix/sub-confusion.data")),
        "transposition": ast.literal_eval(
            read_from_file("Dataset/Spelling Dataset/test/Confusion Matrix/Transposition-confusion.data"))
    }
