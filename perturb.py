import os

import pandas as pd


class RULE:
    name = None
    rule_map = None

    def __init__(self, name, rule_map):
        self.rule_map = rule_map
        self.name = name


class RULES:
    rules = {}

    def __init__(self):
        # Example usage
        rules_directory = 'rules'
        self.rules = self.read_files_in_directory(rules_directory)

    def get_rules(self):
        return self.rules

    @staticmethod
    def read_files_in_directory(directory_path):
        file_contents = {}

        if not os.path.exists(directory_path):
            return file_contents

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r+", encoding='utf-8') as rulefile:
                    sub_dict = {}
                    for line in rulefile:
                        [s1, s2] = line.strip().split(':')
                        if s1 not in sub_dict:
                            sub_dict[s1] = s2
                    file_contents[filename.split(".")[0]] = sub_dict

        return file_contents


class Perturb:
    rules = None
    dataframe = pd.DataFrame

    def __init__(self):
        x = RULES()
        self.rules = x.get_rules()

    def runner(self, dataframe):
        self.dataframe = dataframe
        for index, row in self.dataframe.iterrows():
            # Access row values using column names
            # column1_value = row['column_name1']
            for rulename, rulemap in self.rules.items():
                pert_line = self.perturb(rulename, row['tweet'])
                self.dataframe.at[index, rulename] = pert_line

    def perturb(self, rule, line):
        # sanitize line
        line = line.strip().replace("\n", "").replace("\r", "")
        sub_dict = self.rules[rule]

        for key in sub_dict.keys():
            if key in line:
                line = line.replace(key, sub_dict[key], 100)

        return line

    def get(self):
        return self.dataframe


if __name__ == '__main__':
    pert = Perturb()

    # print(pert.perturb("CHARACTER_COMBINATION", "Suck his dick and clit"))

    # Abuse Perturbation
    abuse_df = pd.read_csv("datasets/original/abuse.csv")
    abuse_df = abuse_df[['class', 'tweet']]
    abuse_df = abuse_df[abuse_df['class'] == 1]
    abuse_df['tweet'] = abuse_df['tweet'].str.replace('\n', '')
    abuse_df['tweet'] = abuse_df['tweet'].str.replace('\r', '')

    # print(abuse_df)
    pert.runner(abuse_df)
    result = pert.get()
    result.to_csv("datasets/perturbed/abuse.csv", index=False)

    # Spam Perturbation
    spam_df = pd.read_csv("datasets/original/spam.csv", encoding="ISO-8859-1")
    spam_df = spam_df[['v1', 'v2']]
    spam_df = spam_df[spam_df['v1'] == 'spam']
    spam_df.rename(columns={'v1': 'class'}, inplace=True)
    spam_df.rename(columns={'v2': 'tweet'}, inplace=True)
    spam_df['tweet'] = spam_df['tweet'].str.replace('\n', '')
    spam_df['tweet'] = spam_df['tweet'].str.replace('\r', '')

    # print(spam_df)
    pert.runner(spam_df)
    result = pert.get()
    result.to_csv("datasets/perturbed/spam.csv", index=False)

    # Porn Perturbation
    porn_df = pd.DataFrame(columns=["class", "tweet"])
    with open("datasets/original/porn.txt", "r+", encoding="utf-8") as pornfile:
        index = 0
        for line in pornfile.readlines():
            line = line.strip().removeprefix("He: ").removeprefix("She: ")
            porn_df.loc[index] = [0, line]
            index += 1
    porn_df['tweet'] = porn_df['tweet'].str.replace('\n', '')
    porn_df['tweet'] = porn_df['tweet'].str.replace('\r', '')

    # print(porn_df)
    pert.runner(porn_df)
    result = pert.get()
    result.to_csv("datasets/perturbed/porn.csv", index=False)

