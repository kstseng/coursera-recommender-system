import pandas as pd
import numpy as np

A1Ratings = pd.read_csv('/Users/kaishentseng/Documents/coursera/recommender-system/week2/A1Ratings.csv', index_col=0)

#--- mean rating
col_mean = A1Ratings.mean(axis=0)
max(col_mean)]
col_mean.sort(ascending=False)
col_mean[0:5]

#--- % of rating 4+
percent_4_plus = A1Ratings.apply(lambda x : float(sum(x >= 4))/sum(~np.isnan(x)))

percent_4_plus.sort(ascending=False)
percent_4_plus[0:5]

#--- number of rating
num_of_rating = (~np.isnan(A1Ratings)).sum(0)
num_of_rating.sort(ascending=False)
num_of_rating[0:5]

#--- star wars 
starwars = A1Ratings['260: Star Wars: Episode IV - A New Hope (1977)'].apply(lambda x: 0 if np.isnan(x) else 1)
raiders  = A1Ratings['1198: Raiders of the Lost Ark (1981)'].apply(lambda x: 0 if np.isnan(x) else 1)
float(starwars.dot(raiders))/sum(starwars)

percent = []
compare_col = A1Ratings.columns.drop('260: Star Wars: Episode IV - A New Hope (1977)')
for col in compare_col:
    movie = A1Ratings[col].apply(lambda x: 0 if np.isnan(x) else 1)
    percent.append(float(starwars.dot(movie))/sum(starwars))
    
percent_np = np.array(percent)
idx = np.argsort(percent_np)
compare_col[idx[-1]]
compare_col[idx[-2]]
compare_col[idx[-3]]
compare_col[idx[-4]]
compare_col[idx[-5]]
