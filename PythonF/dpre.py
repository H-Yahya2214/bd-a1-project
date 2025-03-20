import pandas as pd
import sys
import subprocess

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])  

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    selected_columns = ["series_title", "released_year", "genre", "imdb_rating", "meta_score", "gross"]
    df = df[selected_columns]

    bins = [0, 5, 7, 8.5, 10]
    labels = ["Poor", "Average", "Good", "Excellent"]
    df["imdb_category"] = pd.cut(df["imdb_rating"], bins=bins, labels=labels)

    output_path = "/home/doc-bd-a1/res_dpre.csv"
    df.to_csv(output_path, index=False)

    subprocess.run(["python3", "eda.py", output_path])
