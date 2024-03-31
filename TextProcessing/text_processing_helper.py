from TextProcessing.controller.text_processing import TextProcessing


class TextProcessingHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_tokens(text):
        return TextProcessing.get_tokens_from_text(text)

    @staticmethod
    def tokens_count(data):
        return TextProcessing.tokens_count(data)

    @staticmethod
    def run_text_processing(data):
        TextProcessing(data).run()
