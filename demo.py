import pandas as pd
from perspectiveAPI import EvaluationMode, PerspectiveAPI


categories = ["abuse", "porn", "spam"]
api = PerspectiveAPI()

for cat in categories:
    input_df = pd.read_csv(f"datasets/perturbed/{cat}.csv", nrows=3)
    input_df = input_df.drop(['class'], axis=1)
    count = 0

    input_df2 = pd.DataFrame(columns=list(input_df.columns))

    for index, row in input_df.iterrows():
        mode = EvaluationMode.TOXIC
        new_row = []
        for index, column in enumerate(list(input_df.columns)):
            if cat == "spam":
                mode = EvaluationMode.SPAM
                score = api.getScore(row.tolist()[index], mode)[0]
            else:
                score = api.getScore(row.tolist()[index], mode)[1]

            if score:
                # print(column, line, score)
                new_row.append(score)
                # input_df2.loc[count] = [row.tolist()[0], score]
                # print(row.tolist()[0], score)

        if new_row:
            input_df2.loc[count] = new_row
            count += 1

    input_df2.to_csv(f"results/demo_{cat}_scores.csv", index=False)