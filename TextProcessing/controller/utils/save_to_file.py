import os


def check(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_tokens_to_file(tokens: list, punctuation=True):
    check("Results/TextProcessing/Tokenization/")
    if punctuation:
        with open("Results/TextProcessing/Tokenization/tokens_with_punctuation.txt", 'w') as file:
            file.write(f"len: {len(tokens)}")
            for items in tokens:
                # file.write('%s\n' % items)
                file.write(f'\n{items}')

    else:
        with open("Results/TextProcessing/Tokenization/tokens_without_punctuation.txt", 'w') as file:
            file.write(f"len: {len(tokens)}")
            for items in tokens:
                file.write(f'\n{items}')

    print("-----------------------------------------------------")
    print("FILE SAVED SUCCESSFULLY")
    print("-----------------------------------------------------")


def save_lower_text_to_file(data):
    check("Results/TextProcessing/Lowercase Folding/")
    with open("Results/TextProcessing/Lowercase Folding/lower_data.txt", 'w') as file:
        file.write(data)

    print("-----------------------------------------------------")
    print("FILE SAVED SUCCESSFULLY")
    print("-----------------------------------------------------")


def save_stemmed_words_to_file(stemmed_words: list):
    check("Results/TextProcessing/Stemming/")
    with open("Results/TextProcessing/Stemming/stemmed_words.txt", 'w') as file:
        file.write(f"len: {len(stemmed_words)}")
        for items in stemmed_words:
            file.write(f'\n{items}')

    print("-----------------------------------------------------")
    print("FILE SAVED SUCCESSFULLY")
    print("-----------------------------------------------------")


def save_words_freq_to_file(words_freq):
    check("Results/TextProcessing/Word Frequency/")
    with open("Results/TextProcessing/Word Frequency/words_frequency.txt", 'w') as file:
        file.write(f'len: {len(words_freq)}')
        for items in words_freq.keys():
            # file.write('%s: %s\n' % items % words_freq[items])
            file.write(f'\n{items}: {words_freq[items]}')

    print("-----------------------------------------------------")
    print("FILE SAVED SUCCESSFULLY")
    print("-----------------------------------------------------")

