class ShowResults:
    def __init__(self):
        pass

    @staticmethod
    def show(params):
        print("\n\n")
        for word in params.keys():
            if len(params[word]) == 0:
                print("----------------------------------------------------------")
                print(f"the word:{word} has no candidates")
                continue

            probabilities = {}
            print(f"word:{word}\t\tcandidates:{params[word].keys()}")
            for candidate in params[word].keys():
                print(f"{params[word][candidate][2]}\tword: {word}\tcandidate: {candidate}\tProbability: "
                      f"{params[word][candidate][3]}")
                print(f"key: {params[word][candidate][0]}\tcheck: {params[word][candidate][1]}\n")
                probabilities[candidate] = params[word][candidate][3]

            print(f"Best candidate for: {word} -> {max(probabilities, key=lambda x: probabilities[x])}")
            print("----------------------------------------------------------")
