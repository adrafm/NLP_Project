import re
from TextProcessing.model.Sentence import Sentence

DEFAULT_SENTENCE_BOUNDARIES = ['(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)', '\.{2,}', '\!+', '\:+', '\?+']


def sentencize(raw_input_document, sentence_boundaries=DEFAULT_SENTENCE_BOUNDARIES, delimiter_token='<SPLIT>'):
    working_document = raw_input_document
    punctuation_patterns = sentence_boundaries

    for punctuation in punctuation_patterns:
        working_document = re.sub(punctuation, '\g<0>'+delimiter_token, working_document, flags=re.UNICODE)

    list_of_string_sentences = [x.strip() for x in working_document.split(delimiter_token) if x.strip() != ""]
    list_of_sentences = []

    previous = None
    for sent in list_of_string_sentences:
        start_pos = raw_input_document.find(sent)
        end_pos = start_pos + len(sent)
        new_sentence = Sentence(start_pos, end_pos, raw_input_document)
        list_of_sentences.append(new_sentence)

        if previous is None:
            previous = new_sentence
        else:
            previous.next_sentence = new_sentence
            new_sentence.previous_sentence = previous
            previous = new_sentence

    return list_of_sentences
