def count_words(tokens: list):
    word_freq = {}
    for word in tokens:
        word = str(word)
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    return word_freq


def count_all_words(tokens: list):
    # return len(set(tokens))
    return len(count_words(tokens))
