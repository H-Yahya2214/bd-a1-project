import pandas as pd
import sys
import matplotlib.pyplot as plt
import subprocess

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])  

    plt.figure(figsize=(10, 5))
    df["imdb_category"].value_counts().plot(kind="bar", color=["red", "blue", "green", "purple"])
    plt.xlabel("IMDb Rating Category")
    plt.ylabel("Count of Movies")
    plt.title("Distribution of IMDb Ratings")

    output_path = "/home/doc-bd-a1/vis.png"
    plt.savefig(output_path)

    subprocess.run(["python3", "model.py", "/home/doc-bd-a1/res_dpre.csv"])
