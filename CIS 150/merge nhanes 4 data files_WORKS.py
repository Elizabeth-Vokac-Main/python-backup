import pandas as pd
import pyreadstat
import os

# Change to the directory containing the .XPT files
os.chdir(r"c:\Users\lavok\Desktop\Students\HomeworkDoctors\James Snow\Bio Final Project\NHANES xpt")

# List the files in the current directory to verify
print("Files in directory:", os.listdir())

# Load .XPT files using relative paths
trans_EMA, meta1 = pyreadstat.read_xport("TGEMA_H.XPT")
zn_lab_results, meta2 = pyreadstat.read_xport("CUSEZN_H.XPT")
alp_lab_results, meta3 = pyreadstat.read_xport("BIOPRO_H.XPT")
cd_questionnaire, meta4 = pyreadstat.read_xport("MCQ_H.XPT")

print(trans_EMA.head())
print(zn_lab_results.head())
print(alp_lab_results.head())
print(cd_questionnaire.head())




# Check for missing values in each file before merging
print("Missing values in trans_EMA:")
print(trans_EMA.isnull().sum())

print("Missing values in zn_lab_results:")
print(zn_lab_results.isnull().sum())

print("Missing values in alp_lab_results:")
print(alp_lab_results.isnull().sum())

print("Missing values in cd_questionnaire:")
print(cd_questionnaire.isnull().sum())

# Handle missing values (example: fill missing values with 0)
trans_EMA_filled = trans_EMA.fillna(0)
zn_lab_results_filled = zn_lab_results.fillna(0)
alp_lab_results_filled = alp_lab_results.fillna(0)
cd_questionnaire_filled = cd_questionnaire.fillna(0)

# Merge files after handling missing values
merged_data = pd.merge(trans_EMA_filled, zn_lab_results_filled, on="SEQN")
merged_data = pd.merge(merged_data, alp_lab_results_filled, on="SEQN")
merged_data = pd.merge(merged_data, cd_questionnaire_filled, on="SEQN")

# Check the merged data
print(merged_data.head())

# Save the merged data to a new CSV file
merged_data.to_csv("merged_data.csv", index=False)
