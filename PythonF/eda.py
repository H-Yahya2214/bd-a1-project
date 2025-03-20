import pandas as pd
import sys
import subprocess

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])  

    most_common_genre = df["genre"].mode()[0]
    with open("/home/doc-bd-a1/eda-in-1.txt", "w") as f:
        f.write(f"Most common genre: {most_common_genre}\n")

    avg_rating = df["imdb_rating"].mean()
    with open("/home/doc-bd-a1/eda-in-2.txt", "w") as f:
        f.write(f"Average IMDb rating: {avg_rating:.2f}\n")

    df["gross"] = df["gross"].replace(",", "", regex=True).astype(float)  
    highest_grossing_movie = df.loc[df["gross"].idxmax(), "series_title"]

    with open("/home/doc-bd-a1/eda-in-3.txt", "w") as f:
        f.write(f"Highest grossing movie: {highest_grossing_movie}\n")

    subprocess.run(["python3", "vis.py", "/home/doc-bd-a1/res_dpre.csv"])
