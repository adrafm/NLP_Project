class ShowResults:
    def __init__(self):
        pass

    @staticmethod
    def show_tokens(tokens):
        print(tokens)

    @staticmethod
    def show_lowercase_folded_text(text):
        print(text)

    @staticmethod
    def show_stemmed_words(stemmed_words):
        print(stemmed_words)

    @staticmethod
    def show_words_count(words_count):
        print(f"words count: {words_count}")

    @staticmethod
    def show_words_freq(words_freq):
        print(f"words freq: {words_freq}")
