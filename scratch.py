import pandas as pd


abuse = pd.read_csv("results/orig_abuse_scores.csv")
# print(abuse)
sum, count = 0, 0
for text in list(abuse['text']):
   sum += len(text)
   count += 1
print(sum/count)

spam = pd.read_csv("results/orig_spam_scores.csv")
# print(spam)
sum, count = 0, 0
for text in list(spam['text']):
   sum += len(text)
   count += 1
print(sum/count)
# cols = []
# for column in pert_abuse.columns:
#     if 'score' in column:
#         cols.append(column)
#
# pert_abuse = pert_abuse[cols]
# new_cols = []
# threshold = 0.2
#
# for col in cols:
#     if col == "score":
#         continue
#
#     newcol = f"{col}_res".replace("_score", "")
#     new_cols.append(newcol)
#
#     (pert_abuse['score'] - pert_abuse[col]) / pert_abuse['score'] >= threshold
#     pert_abuse[newcol] = pert_abuse[newcol].astype(int)
#     print(f"{newcol} EFR = {pert_abuse[pert_abuse[newcol] == 1].shape[0] / pert_abuse.shape[0]}")
