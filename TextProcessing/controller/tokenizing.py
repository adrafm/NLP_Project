from TextProcessing.model.Document import Document


def tokenizing_without_punctuation(data):
    document = Document(data)
    sentences = document.sentences
    tokens = []
    for sentence in sentences:
        tokens += [token for token in sentence.tokens if token != ""]

    return tokens


def tokenizing_with_punctuation(data):
    import re
    return re.findall(r'\w+|[^\s\w]+', data)
