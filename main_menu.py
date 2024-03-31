from TextProcessing.menu_helper import MenuHelper

class MainMenu:
    def __init__(self):
        pass

    @staticmethod
    def create_menu():
        print("\n")
        print("------------------------------------------------------------------")
        print("\t\t\tMain Menu")
        print("------------------------------------------------------------------")
        print("\n")

        return int(input(f"1. Text Processing\n2. Spell Correction\n3. Text Classification\n4. Exit\nchoose: "))

    @staticmethod
    def create_text_processing_menu():
        return MenuHelper.run_text_processing_menu()
