from TextProcessing.controller.sentence_tokenization import tokenize


class Sentence:
    def __init__(self, start_position, end_position, raw_document_reference):
        self.start_pos = int(start_position)
        self.end_pos = int(end_position)
        self._document_string = raw_document_reference
        self.next_sentence = None
        self.previous_sentence = None
        self.tokens = tokenize(self._document_string[self.start_pos:self.end_pos])
        self._index = 0
