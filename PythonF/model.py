import pandas as pd
import sys
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])  
 
    df["meta_score"] = pd.to_numeric(df["meta_score"], errors="coerce")
    df["imdb_rating"] = pd.to_numeric(df["imdb_rating"], errors="coerce")
    df["gross"] = df["gross"].replace(",", "", regex=True).astype(float)

    df.dropna(subset=["imdb_rating", "meta_score", "gross"], inplace=True)

    X = df[["imdb_rating", "meta_score", "gross"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    cluster_counts = df["cluster"].value_counts()

    output_path = "/home/doc-bd-a1/k.txt"
    with open(output_path, "w") as f:
        for cluster, count in cluster_counts.items():
            f.write(f"Cluster {cluster}: {count} movies\n")
