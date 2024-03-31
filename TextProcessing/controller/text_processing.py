from TextProcessing.controller.counting_words import count_words, count_all_words
from TextProcessing.controller.tokenizing import tokenizing_with_punctuation
from TextProcessing.controller.tokenizing import tokenizing_without_punctuation
from TextProcessing.controller.utils.read_file import read_from_file
from TextProcessing.controller.utils.save_to_file import save_tokens_to_file, save_lower_text_to_file, \
    save_stemmed_words_to_file, save_words_freq_to_file
from TextProcessing.view.show_results import ShowResults


class TextProcessing:
    def __init__(self, num: int):
        self.num = num
        self.data = read_from_file()
        self.tokens_with_punctuation = self.get_tokens_with_punctuation()
        self.tokens_without_punctuation = self.get_tokens_without_punctuation()
        self.stemmed_words = self.stemming()
        self.lower_data = self.lowercase_folding()
        self.words_freq, self.words_count = self.counting_tokens()

        # self.save_to_file()

    def check(self):
        self.tokens_with_punctuation = [i for i in self.tokens_with_punctuation if str(i).strip(' ') != '']

    def save_tokens(self):
        save_tokens_to_file(self.tokens_with_punctuation)
        save_tokens_to_file(self.tokens_without_punctuation, False)

    def save_lower_text(self):
        save_lower_text_to_file(self.lower_data)

    def save_stemmed_words(self):
        save_stemmed_words_to_file(self.stemmed_words)

    def save_words_freq(self):
        save_words_freq_to_file(self.words_freq)

    def save_to_file(self):
        self.check()
        save_tokens_to_file(self.tokens_with_punctuation)
        save_tokens_to_file(self.tokens_without_punctuation, False)

        save_lower_text_to_file(self.lower_data)
        save_stemmed_words_to_file(self.stemmed_words)
        save_words_freq_to_file(self.words_freq)

    def get_tokens_without_punctuation(self):
        return tokenizing_without_punctuation(self.data)

    def get_tokens_with_punctuation(self):
        return tokenizing_with_punctuation(self.data)

    @staticmethod
    def get_tokens_from_text(data):
        return tokenizing_with_punctuation(data)

    def stemming(self):
        from nltk.stem import PorterStemmer
        ps = PorterStemmer()

        return [ps.stem(str(word)) for word in self.tokens_with_punctuation]

    def lowercase_folding(self):
        return self.data.lower()

    def counting_tokens(self):
        word_freq = count_words(self.tokens_with_punctuation)
        words_count = count_all_words(self.tokens_with_punctuation)

        return word_freq, words_count

    @staticmethod
    def tokens_count(data):
        return count_words(TextProcessing.get_tokens_from_text(data))

    def run(self):
        if self.num == 1:
            ShowResults.show_tokens(self.tokens_with_punctuation)
            ShowResults.show_tokens(self.tokens_without_punctuation)

            self.save_tokens()
        elif self.num == 2:
            ShowResults.show_lowercase_folded_text(self.lower_data)

            self.save_lower_text()
        elif self.num == 3:
            ShowResults.show_words_count(self.words_count)
            ShowResults.show_words_freq(self.words_freq)

            self.save_words_freq()
        elif self.num == 4:
            ShowResults.show_stemmed_words(self.stemmed_words)

            self.save_stemmed_words()
