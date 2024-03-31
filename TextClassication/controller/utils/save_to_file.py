import os


def check(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_results_to_file(results, true_labels, accuracy):
    check("Results/TextClassification/")
    with open("Results/TextClassification/results.txt", 'w') as file:
        file.write(f"Accuracy: {accuracy}\n")
        for item in results.keys():
            file.write(f"---------------------------------------------------\n")
            file.write(f"File: {item}\nPredicted Label: {results[item]},\t True Label: {true_labels[item]}\n")
            file.write(f"---------------------------------------------------\n")

    print("-----------------------------------------------------")
    print("FILE SAVED SUCCESSFULLY")
    print("-----------------------------------------------------")