#!/usr/bin/env python

# for each zip file in the current directory:
#     extract zip file
#     load answer.csv into dataframe
#     calculate score
#     save score
# save all scores to csv file

import zipfile
import os
import pandas as pd

import sys
import os.path
from sklearn.metrics import f1_score, recall_score, precision_score, classification_report
import numpy as np

df_truth = pd.read_csv("truth.csv")

scores = []
directory = r'.'
for filename in os.listdir(directory):
    if filename.endswith(".zip"):
        print(os.path.join(directory, filename))
        with zipfile.ZipFile(os.path.join(directory, filename),"r") as zip_ref:
            zip_ref.extractall("targetdir")
            df_answer = pd.read_csv("targetdir/answer.csv")

            y_true_1 = np.array(df_truth["Sub1_Toxic"])
            y_true_2 = np.array(df_truth["Sub2_Engaging"])
            y_true_3 = np.array(df_truth["Sub3_FactClaiming"])
            y_pred_1 = np.array(df_answer["Sub1_Toxic"])
            y_pred_2 = np.array(df_answer["Sub2_Engaging"])
            y_pred_3 = np.array(df_answer["Sub3_FactClaiming"])

            report = classification_report(y_true_1, y_pred_1, output_dict=True)
            precision_score_1 = report["macro avg"]["precision"]
            recall_score_1 = report["macro avg"]["recall"]
            f1_score_1 = 0
            if precision_score_1+recall_score_1 > 0:
                f1_score_1 = 2*precision_score_1*recall_score_1/(precision_score_1+recall_score_1)

            report = classification_report(y_true_2, y_pred_2, output_dict=True)
            precision_score_2 = report["macro avg"]["precision"]
            recall_score_2 = report["macro avg"]["recall"]
            f1_score_2 = 0
            if precision_score_2+recall_score_2 > 0:
                f1_score_2 = 2*precision_score_2*recall_score_2/(precision_score_2+recall_score_2)

            report = classification_report(y_true_3, y_pred_3, output_dict=True)
            precision_score_3 = report["macro avg"]["precision"]
            recall_score_3 = report["macro avg"]["recall"]
            f1_score_3 = 0
            if precision_score_3+recall_score_3 > 0:
                f1_score_3 = 2*precision_score_3*recall_score_3/(precision_score_3+recall_score_3)

            scores.append({
            "ID": filename,
            "Sub1_F1": f1_score_1,
            "Sub1_P":precision_score_1,
            "Sub1_R":recall_score_1,

            "Sub2_F1":f1_score_2,
            "Sub2_P":precision_score_2,
            "Sub2_R":recall_score_2,

            "Sub3_F1":f1_score_3,
            "Sub3_P":precision_score_3,
            "Sub3_R":recall_score_3
            })
print(scores)
df = pd.DataFrame(scores)
df.to_csv("all_scores.csv", index=False)
