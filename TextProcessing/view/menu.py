class Menu:
    def __init__(self):
        pass

    @staticmethod
    def create_text_processing_menu() -> int:
        return int(input(f"1. Tokenizing\n2. LowerCase Folding\n3. Counting Tokens\n4. Stemming\nchoose: "))
