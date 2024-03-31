import re
from TextProcessing.model.Token import Token

DEFAUT_SENTENCE_BOUNDATIES = ['(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)', '\.{2,}', '\!+', '\:+', '\?+']

DEFAULT_PUNCTUATIONS = DEFAUT_SENTENCE_BOUNDATIES + ['\,+', '\_+', '\-+', r'\(|\)|\[|\]|{|\}|\<|\>']


def tokenize(raw_input_sentence, join_split_text = True, split_text_char='\-', punctuation_patterns=DEFAULT_PUNCTUATIONS,
             split_charachters=r'\s|\t|\n|\r', delimiter_token='<SPLIT>'):
    working_sentence = raw_input_sentence
    if join_split_text:
        working_sentence = re.sub('[a-z]+('+split_text_char+'[\n])[a-z]+', '', working_sentence)

    for punctuation in punctuation_patterns:
        working_sentence = re.sub(punctuation, "\g<0>", working_sentence)

    working_sentence = re.sub(split_charachters, delimiter_token, working_sentence)
    list_of_token_strings = [x.strip() for x in working_sentence.split(delimiter_token) if x.strip() != ""]

    previous = Token(0, 0, raw_input_sentence, SOS=True)
    list_of_tokens = [previous]
    for token in list_of_token_strings:
        start_pos = raw_input_sentence.find(token)
        end_pos = start_pos + len(token)
        new_token = Token(start_pos, end_pos, raw_input_sentence)
        list_of_tokens.append(new_token)
        previous.next_token = new_token
        new_token.previous_token = previous
        previous = new_token

    if not previous.SOS:
        eos = Token(len(raw_input_sentence), len(raw_input_sentence), raw_input_sentence, EOS=True)
        previous.next_token = eos
        eos.previous_token = previous
        list_of_tokens.append(eos)

    return list_of_tokens
