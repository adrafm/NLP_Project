class Token:
    def __init__(self, start_position, end_position, raw_sentence_reference, SOS=False, EOS=False):
        self.start_pos = int(start_position)
        self.end_pos = int(end_position)
        self._sentence_string = raw_sentence_reference
        self.next_token = None
        self.previous_token = None
        self.SOS = SOS
        self.EOS = EOS

    def get(self):
        # if self.SOS:
        #     return '<SOS>'
        #
        # elif self.EOS:
        #     return '<EOS>'
        #
        # else:
        return self._sentence_string[self.start_pos:self.end_pos]

    def __repr__(self):
        return self.get()

    def __str__(self):
        return self.get()

    def __eq__(self, other):
        return self.get() == other
