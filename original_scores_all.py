import pandas as pd
from perspectiveAPI import EvaluationMode, PerspectiveAPI

THRESHOLD = 0.6
results = []
ITERATIONS = 500
cols = ['text', 'label', 'tox_score', 'category']

api = PerspectiveAPI()


def runner(name):
    df = pd.read_csv(f"datasets/perturbed/{name}.csv")
    df = df[['tweet']]
    df2 = pd.DataFrame(columns=["text", "score"])
    count = 0

    for index, row in df.iterrows():
        mode = EvaluationMode.TOXIC
        if name == "spam":
            mode = EvaluationMode.SPAM
            score = api.getScore(row.tolist()[0], mode)[0]
        else:
            score = api.getScore(row.tolist()[0], mode)[1]

        if (score and
                score >= THRESHOLD):
            # print(column, line, score)
            df2.loc[count] = [row.tolist()[0], score]
            print(row.tolist()[0], score)
            count += 1
        if count > ITERATIONS:
            break

    df2.to_csv(f"results/orig_{name}_scores.csv", index=False)


if __name__ == '__main__':
    names = ["abuse", "spam", "porn"]
    for name in names:
        runner(name)