import pandas as pd
import sys
import subprocess

if __name__ == "__main__":
    file_path = sys.argv[1]  
    df = pd.read_csv(file_path)  

    output_path = "/home/doc-bd-a1/res_load.csv"
    df.to_csv(output_path, index=False)  

    subprocess.run(["python3", "dpre.py", output_path])
