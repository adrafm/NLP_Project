import os


def check(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_results_to_file(params):
    check("Results/SpellCorrection/")
    with open("Results/SpellCorrection/results.txt", 'w') as file:
        for word in params.keys():
            if len(params[word]) == 0:
                file.write(f"the word:{word} has no candidates\n")
                file.write("----------------------------------------------------------\n")
                continue

            probabilities = {}
            file.write(f"word:{word}\t\tcandidates:{params[word].keys()}\n")
            for candidate in params[word].keys():
                file.write(f"{params[word][candidate][2]}\tword: {word}\tcandidate: {candidate}\tProbability: "
                      f"{params[word][candidate][3]}\n")
                file.write(f"key: {params[word][candidate][0]}\tcheck: {params[word][candidate][1]}\n\n")
                probabilities[candidate] = params[word][candidate][3]

            file.write(f"Best candidate for: {word} -> {max(probabilities, key=lambda x: probabilities[x])}\n")
            file.write("----------------------------------------------------------\n")

    print("-----------------------------------------------------")
    print("FILE SAVED SUCCESSFULLY")
    print("-----------------------------------------------------")
