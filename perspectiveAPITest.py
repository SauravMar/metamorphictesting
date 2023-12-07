from perspectiveAPI import EvaluationMode, PerspectiveAPI

with open("saurav/datasets/original/porn.txt", "r+", encoding="utf8") as infile:
    counter = 0
    api = PerspectiveAPI()

    for line in infile:
        score = api.getScore(line.strip(), EvaluationMode.BOTH)
        print("Line: ", line, f"Spam Score: {score[0]}\tToxic Score: {score[1]}\n")

        if counter == 10:
            break
        else:
            counter += 1