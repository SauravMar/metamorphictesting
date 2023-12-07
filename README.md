- Find all metamorphic relations that can be applied
    - Check literature and perform survey
    - list out all relations

- Collect dataset for project -> better if we can get datasets separately for porn, malicious ads, hate speech
    - Some data is included. We can probably use that. It would be better if we had multiple types of data

- Perform Perturbations on Input and generate perturbed inputs
    - Write transformation rules and run code to generate transformed lines using these rules.
    - Initially, run perturbations per rule and then combine a few perturbations
    - Collect all such data separately and store properly

- Run toxicity code on it and find EFR under various forms of Perturbations separately and together
    - Run toxicity analysis on original dataset. We can filter out texts from original that aren't too toxic.
    - Run same analysis on perturbed dataset and collect metrics.
    - Compare the two and any difference beyond a threshold indicates error. Calculate EFR using different thresholds and see their impact.

- Check performance of off-the-shelf toxicity detector on original dataset and the perturbed inputs -> diff in toxic scores show models inability to handle MTTM
    - Train model with MTTM inputs and then run original + perturbed models on dataset to show improvement

=====================================================================================================================================
Spam.CSV = https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/