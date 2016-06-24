import pandas as pd

A1Ratings = pd.read_csv('/Users/kaishentseng/Documents/coursera/recommender-system/week2/A1Ratings.csv', index_col=0)

#---
col_mean = A1Ratings.mean(axis=0)
max(col_mean)]
col_mean.sort(ascending=False)
col_mean[0:5]

#---