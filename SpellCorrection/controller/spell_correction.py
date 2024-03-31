from collections import Counter
from SpellCorrection.controller.utils.read_file import read_dataset_file, read_dictionary_file, \
    read_spell_test_set_file, read_confusion_matrices_file
from SpellCorrection.controller.utils.save_to_file import save_results_to_file
from SpellCorrection.view.show_results import ShowResults
import enchant


class SpellCorrection:
    def __init__(self):
        self.dataset = read_dataset_file()
        self.dictionary = read_dictionary_file()
        self.dataset_words = self.get_words_dic(self.dataset)
        self.dictionary_words = self.get_words_dic(self.dictionary)
        self.test_set = read_spell_test_set_file()
        self.test_vocabs = self.get_words_dic(self.test_set)
        self.confusion_matrices = read_confusion_matrices_file()
        self.params = {}
        self.run()
        ShowResults.show(self.params)
        self.save_to_file()
        # self.show()

    def save_to_file(self):
        save_results_to_file(self.params)

    @staticmethod
    def get_words(data):
        import re
        return re.findall(r'\w+', data.lower())

    def get_words_dic(self, data):
        return Counter(self.get_words(data))

    def unigram_language_model(self, word):
        n = sum(self.dataset_words.values())
        return self.dataset_words[word] / n

    @staticmethod
    def get_generated_candidates(word):
        d = enchant.Dict("en_US")
        return list(d.suggest(word))

    @staticmethod
    def get_edit_distance_1(word: str, candidate):
        from strsimpy.damerau import Damerau
        return Damerau().distance(candidate, word.lower()) < 2

        # words = [i for i in words if 0 <= enchant.utils.levenshtein(i, word) <= 2]

    def get_candidates(self, word):
        words = self.get_generated_candidates(word)
        # words = [i for i in words if self.get_edit_distance_1(word, i) and ' ' not in i]
        words = [i for i in words if self.get_edit_distance_1(word, i) and str(i).isalpha()]
        if word not in words and self.check_word_exist_in_dictionary(word):
            words.append(word)

        return words

    def check_word_exist_in_dictionary(self, word):
        return word in self.dictionary_words

    # def get_correction(self, word):
    #     return max(self.get_candidates(word), key=self.unigram_language_model)

    # def run(self):
    #     for word in self.test_vocabs:
    #         candidates = self.get_candidates(word)
    #         if len(candidates) == 0:
    #             print("----------------------------------------------------------")
    #             print(f"the word:{word} has no candidates")
    #             continue
    #         probabilities = {}
    #         print("----------------------------------------------------------")
    #         print(f"word:{word}\t\tcandidates:{candidates}")
    #         for candidate in candidates:
    #             probability = 0.95
    #             # if not (candidate in self.dictionary_words or candidate == word):
    #             if not (candidate == word):
    #                 probability = self.assign_probability(word.lower(), candidate.lower())
    #             else:
    #                 print(f"the word itself:{word}\t\tcandidate:{candidate}")
    #             # probability = 0.95
    #             # if candidate not in self.dictionary_words:
    #             #     probability = self.assign_probability(word, candidate)
    #
    #             probabilities[candidate] = probability * self.unigram_language_model(candidate)
    #         print(f"{word} -> {max(probabilities, key=lambda x: probabilities[x])}")

    def run(self):
        global op_type, check, key
        for word in self.test_vocabs:
            candidates = self.get_candidates(word)
            self.params[word] = {}
            if len(candidates) == 0:
                continue
            probabilities = {}
            for candidate in candidates:
                probability = 0.95
                if candidate != word:
                    probability, op_type, key, check = self.assign_probability(word.lower(), candidate.lower())

                probabilities[candidate] = probability * self.unigram_language_model(candidate)
                self.params[word][candidate] = key, check, op_type, probabilities[candidate]

    # def show(self):
    #     print("\n\n")
    #     for word in self.params.keys():
    #         if len(self.params[word]) == 0:
    #             print("----------------------------------------------------------")
    #             print(f"the word:{word} has no candidates")
    #             continue
    #
    #         probabilities = {}
    #         print(f"word:{word}\t\tcandidates:{self.params[word].keys()}")
    #         for candidate in self.params[word].keys():
    #             print(f"{self.params[word][candidate][2]}\tword: {word}\tcandidate: {candidate}\tProbability: "
    #                   f"{self.params[word][candidate][3]}")
    #             print(f"key: {self.params[word][candidate][0]}\tcheck: {self.params[word][candidate][1]}\n")
    #             probabilities[candidate] = self.params[word][candidate][3]
    #
    #         print(f"Best candidate for: {word} -> {max(probabilities, key=lambda x: probabilities[x])}")
    #         print("----------------------------------------------------------")

    # def assign_probability(self, word, candidate):
    #     def check_insertion():
    #         return len(candidate) < len(word)
    #
    #     def check_deletion():
    #         return len(candidate) > len(word)
    #
    #     def check_substitution():
    #         import Levenshtein
    #         return Levenshtein.distance(word, candidate) == 1 and len(word) == len(candidate)
    #
    #     positions = self.find_position_of_difference(word, candidate)
    #     if check_insertion():
    #         print(f"insertion\tword:{word}\tcandidate:{candidate}")
    #         key, check = self.get_insertion_key(word, candidate, positions[0])
    #         print(f"key: {key}\t\tcheck: {check}\n")
    #
    #         return self.confusion_matrices["insertion"][key] / self.dataset.count(check)
    #     elif check_deletion():
    #         print(f"deletion\tword:{word}\tcandidate:{candidate}")
    #         if len(positions) != 0:
    #             key, check = self.get_deletion_key(candidate, positions[0])
    #         else:
    #             key, check = self.get_deletion_key(candidate, len(candidate)-1)
    #         print(f"key: {key}\t\tcheck: {check}\n")
    #
    #         return self.confusion_matrices["deletion"][key] / self.dataset.count(check)
    #     elif check_substitution():
    #         print(f"substitution\tword:{word}\tcandidate:{candidate}")
    #         key, check = self.get_substitution_key(word, candidate, positions[0])
    #         print(f"key: {key}\t\tcheck: {check}\n")
    #
    #         return self.confusion_matrices["substitution"][key] / self.dataset.count(check)
    #     else:
    #         print(f"transposition\tword:{word}\tcandidate:{candidate}")
    #         key, check = self.get_transposition_key(candidate, positions)
    #         print(f"key: {key}\t\tcheck: {check}\n")
    #
    #         return self.confusion_matrices["transposition"][key] / self.dataset.count(check)
    #

    def assign_probability(self, word, candidate):
        def check_insertion():
            return len(candidate) < len(word)

        def check_deletion():
            return len(candidate) > len(word)

        def check_substitution():
            import Levenshtein
            return Levenshtein.distance(word, candidate) == 1 and len(word) == len(candidate)

        positions = self.find_position_of_difference(word, candidate)
        if check_insertion():
            # print(f"insertion\tword:{word}\tcandidate:{candidate}")
            key, check = self.get_insertion_key(word, candidate, positions[0])
            # print(f"key: {key}\t\tcheck: {check}\n")

            return self.confusion_matrices["insertion"][key] / self.dataset.count(check), "insertion", key, check
        elif check_deletion():
            # print(f"deletion\tword:{word}\tcandidate:{candidate}")
            if len(positions) != 0:
                key, check = self.get_deletion_key(candidate, positions[0])
            else:
                key, check = self.get_deletion_key(candidate, len(candidate)-1)
            # print(f"key: {key}\t\tcheck: {check}\n")

            return self.confusion_matrices["deletion"][key] / self.dataset.count(check), "deletion", key, check
        elif check_substitution():
            # print(f"substitution\tword:{word}\tcandidate:{candidate}")
            key, check = self.get_substitution_key(word, candidate, positions[0])
            # print(f"key: {key}\t\tcheck: {check}\n")

            return self.confusion_matrices["substitution"][key] / self.dataset.count(check), "substitution", key, check
        else:
            # print(f"transposition\tword:{word}\tcandidate:{candidate}")
            key, check = self.get_transposition_key(candidate, positions)
            # print(f"key: {key}\t\tcheck: {check}\n")

            return self.confusion_matrices["transposition"][key] / self.dataset.count(check), "transposition", key, check

    @staticmethod
    def get_transposition_key(candidate, positions, key=""):
        key += candidate[positions[0]]
        key += candidate[positions[1]]

        return key, ''.join([candidate[positions[0]], candidate[positions[1]]])

    @staticmethod
    def get_substitution_key(word, candidate, position, key=""):
        key += word[position]
        key += candidate[position]

        return key, candidate[position]

    @staticmethod
    def get_deletion_key(candidate, position, key=""):
        if position == 0:
            key += candidate[position]
            key += candidate[position+1]

        else:
            key += candidate[position - 1]
            key += candidate[position]

        return key, ''.join([candidate[position-1], candidate[position]]) if position != 0 else ''.join([candidate[position], candidate[position+1]])

    @staticmethod
    def get_insertion_key(word, candidate, position, key=""):
        if position == 0:
            key += candidate[0]
            key += word[0]

        else:
            key += candidate[position - 1]
            key += word[position]

        return key, candidate[position-1] if position != 0 else candidate[0]

    @staticmethod
    def find_position_of_difference(word, candidate):
        # return [index for index, char in enumerate(word) if not candidate[index] == char]
        li = [i for i, (left, right) in enumerate(zip(word, candidate)) if left != right]
        if len(word) > len(candidate) and len(li) == 0:
            return [len(word)-1]

        if len(word) < len(candidate) and len(li) == 0:
            return [len(candidate)-1]

        return li
