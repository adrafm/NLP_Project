from TextClassication.controller.utils.read_file import read_classification_train_files, get_classes_names, \
    get_classes_files_count, \
    read_classification_test_files, read_classification_test_files_using_class
from TextClassication.controller.utils.save_to_file import save_results_to_file
from TextClassication.view.show_results import ShowResults
import numpy as np

from TextProcessing.text_processing_helper import TextProcessingHelper


class TextClassification:
    def __init__(self):
        self.data = read_classification_train_files()
        self.test_data = read_classification_test_files()
        self.classes = get_classes_names()
        self.vocabs = self.create_vocabs()
        self.texts = self.create_texts()
        self.probs = self.assign_class_probability()
        self.params = self.calc_prob()
        self.test_data_with_class = read_classification_test_files_using_class()
        self.true_labels = self.create_true_labels()
        self.test_results = self.run_test()
        self.accuracy = self.evaluate()
        self.save_to_file()
        ShowResults.show(self.test_results, self.true_labels, self.accuracy)

    def save_to_file(self):
        save_results_to_file(self.test_results, self.true_labels, self.accuracy)

    @staticmethod
    def assign_class_probability():
        classes_probs = get_classes_files_count()

        sum_of_probs = sum(classes_probs[key] for key in classes_probs.keys())
        for key in classes_probs:
            classes_probs[key] /= sum_of_probs

        return classes_probs

    def create_texts(self):
        texts = {}
        for key in self.data.keys():
            texts[key] = TextProcessingHelper.tokens_count(data=self.data[key])

        return texts

    def create_vocabs(self):
        data = ' '.join(self.data.values())
        return list(set(TextProcessingHelper.get_tokens(data)))

    def calc_p_word_given_class(self, word, label):
        count = 0
        if word in self.texts[label]:
            count = self.texts[label][word]
        return (count + 1) / (len(self.vocabs) + self.count_text(self.texts[label]))

    @staticmethod
    def count_text(text):
        return sum([text[x] for x in text.keys()])

    def calc_prob(self):
        dic = {}
        for label in self.classes:
            vocab_dic = {}
            for vocab in self.create_vocabs():
                vocab_dic[vocab] = self.calc_p_word_given_class(vocab, label)
            dic[label] = vocab_dic

        return dic

    def run_test(self):
        results = {}
        for filename in self.test_data_with_class:
            file_labels = {}
            for label in self.classes:
                var = np.log10(self.probs[label])
                words = TextProcessingHelper.tokens_count(self.test_data_with_class[filename].value)
                for word in words:
                    if word not in self.params[label]:
                        var += np.log10(self.calc_unknown_word_prob(label))
                        continue
                    var += np.log10(self.params[label][word]) * words[word]
                file_labels[label] = var
            results[filename] = max(file_labels, key=lambda x: file_labels[x])
        return results

    def create_true_labels(self):
        true_labels = {}
        for filename in self.test_data_with_class.keys():
            # true_labels[filename] = list(self.test_data_with_class[filename].keys())[0]
            true_labels[filename] = self.test_data_with_class[filename].label

        return true_labels

    def create_matrix(self):
        pass

    def evaluate(self):
        numerator = 0
        denominator = 0

        for key in self.test_results.keys():
            if self.test_results[key] == self.true_labels[key]:
                numerator += 1
                denominator += 1
                continue
            denominator += 1

        accuracy = numerator / denominator
        return accuracy*100

    def calc_unknown_word_prob(self, label):
        return 1 / (len(self.vocabs) + len(self.texts[label]) + 1)
