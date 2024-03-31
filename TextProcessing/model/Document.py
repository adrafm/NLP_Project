from TextProcessing.controller.document_sentecizing import sentencize


class Document:
    def __init__(self, document_text):
        self.raw = document_text
        self.sentences = sentencize(self.raw)
        self._index = 0
