import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generarea Datelor
np.random.seed(42)
n_users = 1000
n_movies = 100
n_ratings = 10000

user_ids = np.random.randint(1, n_users + 1, n_ratings)
movie_ids = np.random.randint(1, n_movies + 1, n_ratings)
ratings = np.random.randint(1, 6, n_ratings)

data = pd.DataFrame({'User_ID': user_ids, 'Movie_ID': movie_ids, 'Rating': ratings})

# 2. Procesarea Datelor
mean_ratings = data.groupby('Movie_ID')['Rating'].mean()
count_ratings = data.groupby('Movie_ID')['Rating'].count()

top_5_movies = mean_ratings.sort_values(ascending=False).head(5)
low_rated_movies = mean_ratings[count_ratings > 50][mean_ratings < 3.5]

# 3. Vizualizare
plt.figure(figsize=(12, 5))
plt.hist(data['Rating'], bins=5, edgecolor='black', alpha=0.7)
plt.xlabel('Rating')
plt.ylabel('Frecvență')
plt.title('Distribuția Ratingurilor')
plt.show()

plt.figure(figsize=(12, 5))
top_5_movies.plot(kind='bar', color='skyblue')
plt.xlabel('ID Film')
plt.ylabel('Rating Mediu')
plt.title('Top 5 Filme cu Cel Mai Mare Rating Mediu')
plt.show()

plt.figure(figsize=(12, 5))
plt.scatter(count_ratings, mean_ratings, alpha=0.5)
plt.xlabel('Număr de Evaluări')
plt.ylabel('Rating Mediu')
plt.title('Număr de Evaluări vs. Rating Mediu')
plt.show()
