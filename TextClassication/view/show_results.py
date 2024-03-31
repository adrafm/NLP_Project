class ShowResults:
    def __init__(self):
        pass

    @staticmethod
    def show(results, true_labels, accuracy):
        print(f"Accuracy: {accuracy}\n\n")
        for item in results.keys():
            print(f"File: {item}\nPredicted Label: {results[item]},\t True Label: {true_labels[item]}\n")
            print(f"---------------------------------------------------\n")
