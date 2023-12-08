import pandas as pd
from perspectiveAPI import EvaluationMode, PerspectiveAPI
from tqdm import tqdm
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Load files and select top 100 based on scores
files = ["abuse", "porn", "spam"]
api = PerspectiveAPI()

for file in files:
    print(f"------------------- Now doing {file} analysis --------------------")
    results = []
    orig_scores = pd.read_csv(f"results/orig_{file}_scores.csv")
    perturbations = pd.read_csv(f"datasets/perturbed/{file}.csv")

    orig_scores = orig_scores.sort_values('score', ascending=False).head(300)
    print(orig_scores.shape)

    for index in tqdm(range(orig_scores.shape[0])):
        # for index, row in orig_scores.iterrows():
        # print(row)
        row = orig_scores.iloc[[index]].to_dict(orient='records')[0]
        line, score = row["text"], row["score"]
        perturb_form = perturbations.loc[perturbations['tweet'] == line]
        result = {
            "text": line,
            "score": score
        }

        if isinstance(perturb_form, pd.DataFrame):
            perturb_form = perturb_form.drop(columns=['class', 'tweet']).to_dict(orient='records')
            if len(perturb_form) > 0:
                perturb_form = perturb_form[0]

            for rule, perturbed_text in perturb_form.items():
                mode = EvaluationMode.TOXIC
                if file == "spam":
                    mode = EvaluationMode.SPAM
                    score = api.getScore(perturbed_text, mode)[0]
                else:
                    score = api.getScore(perturbed_text, mode)[1]

                result[rule] = perturbed_text
                result[f"{rule}_score"] = score

            results.append(result)
            # break

    print(results)
    result_df = pd.DataFrame(results)
    result_df.to_csv(f"results/pert_{file}_scores.csv", index=False)
