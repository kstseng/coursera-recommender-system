import pandas as pd
import numpy as np
import math

path = '/Users/kaishentseng/Documents/coursera/recommender-system/week3/'
ass2 = pd.read_excel(path+'Assignment 2.xls')

#---
#  part 1
#---
df = ass2.iloc[0:20, 0:10]
user1 = ass2.iloc[0:20:, 13].fillna(0)
user2 = ass2.iloc[0:20:, 14].fillna(0)

user1_profile = []
user2_profile = []
for col in df.columns:
    user1_profile.append(df[col].dot(user1))
    user2_profile.append(df[col].dot(user2))

doc_preference_user1 = []
doc_preference_user2 = []
for r in range(df.shape[0]):
    doc_preference_user1.append(df.iloc[r, :].dot(user1_profile))
    doc_preference_user2.append(df.iloc[r, :].dot(user2_profile))
#Q1
df.index[doc_preference_user1.index(max(doc_preference_user1))]
#Q2
max(doc_preference_user1)
#Q3
sum(pd.Series(doc_preference_user2) < 0)

#---
# part 2
#---
1/math.sqrt(sum(df.iloc[0, :]))
1/math.sqrt(sum(df.iloc[3, :]))

df_w1 = df.copy()
for r in range(df_w1.shape[0]):
    df_w1.iloc[r, :] = df_w1.iloc[r, :]/math.sqrt(sum(df_w1.iloc[r, :]))

user1_profile_w1 = []
user2_profile_w1 = []
for col in df_w1.columns:
    user1_profile_w1.append(df_w1[col].dot(user1))
    user2_profile_w1.append(df_w1[col].dot(user2))


doc_preference_user1_w1 = []
doc_preference_user2_w1 = []
for r in range(df_w1.shape[0]):
    doc_preference_user1_w1.append(df_w1.iloc[r, :].dot(user1_profile_w1))
    doc_preference_user2_w1.append(df_w1.iloc[r, :].dot(user2_profile_w1))
pref_sort = pd.Series(doc_preference_user1_w1).order(ascending=False)
#Q1
df_w1.index[doc_preference_user1_w1.index(pref_sort.iloc[1])]
#Q2
pref_sort.iloc[1]

#---
# part 3
#---
DF = df.apply(sum, 0)
IDF = 1.0/DF

(df_w1.loc['doc1'] * IDF).dot(user1_profile_w1)
#1
(df_w1.loc['doc9'] * IDF).dot(user1_profile_w1)
#2
(df_w1.loc['doc2'] * IDF).dot(user2_profile_w1)

