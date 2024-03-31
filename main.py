from TextClassication.text_classification_helper import TextClassificationHelper
from SpellCorrection.spell_correction_helper import SpellCorrectionHelper
from TextProcessing.text_processing_helper import TextProcessingHelper
from main_menu import MainMenu


def text_processing_function():
    TextProcessingHelper.run_text_processing(MainMenu.create_text_processing_menu())


def spell_correction_function():
    SpellCorrectionHelper.run_spell_correction()


def text_classification_function():
    TextClassificationHelper.run_text_classification()


def main() -> None:
    flag = True
    while flag:
        var = MainMenu.create_menu()
        if var == 1:
            text_processing_function()
        elif var == 2:
            spell_correction_function()
        elif var == 3:
            text_classification_function()
        elif var == 4:
            flag = False

if __name__ == '__main__':
    main()
