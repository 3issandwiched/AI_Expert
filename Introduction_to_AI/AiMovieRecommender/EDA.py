import pandas as pd

df=pd.read_csv("Introduction_to_AI\AiMovieRecommender\imdb_top_1000.csv")

print(df)
print(df.columns)

single_movie = df.iloc[0]

print("🎬 --- SINGLE MOVIE DATA PROFILE --- 🎬\n")
for column in df.columns:
    print(f"📌 {column}: {single_movie[column]}")
