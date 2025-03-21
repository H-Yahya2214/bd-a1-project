Big Data Assignment 1 - Data Processing Pipeline
Project Overview
This project implements a data processing pipeline using Docker. The pipeline runs inside a container based on an Ubuntu image, where a dataset is processed through multiple steps:
1. Loading the dataset.
2. Preprocessing: Data cleaning, transformation, reduction, and discretization.
3. Exploratory Data Analysis (EDA): Extracting insights.
4. Visualization: Creating a graphical representation.
5. Clustering using K-Means (k=3).
6. Copying results from the container to the local machine.
Features
✅ Containerized environment: Runs in an isolated Docker container.
✅ Automated pipeline: Data flows from step to step without manual intervention.
✅ Data processing & transformation: Cleaning, reducing, and structuring data for analysis.
✅ Exploratory Data Analysis (EDA): Generating key insights from the dataset.
✅ Visual representation: Creating a visualization (vis.png).
✅ Machine learning with K-Means: Applying clustering with k=3.
✅ Automatic results extraction: Copies output files from the container to the host machine.
Prerequisites
- Docker installed and running.
- Python 3.x installed inside the Docker container.
- A dataset (CSV format) to process.
Directory Structure
bd-a1/
│── Dockerfile
│── imdb_top_1000.csv  
│── load.py
│── dpre.py
│── eda.py
│── vis.py
│── model.py
│── final.sh
│── service-result/  
│── README.md
Execution Steps
1. Build the Docker Image
Run the following command in the project directory to build the Docker image:
```bash
docker build -t bd-a1-image .
```
2. Run the Docker Container
Create and start a container while mounting the service-result directory to store results:
```bash
docker run -it --name bd-a1-container -v $(pwd)/service-result:/home/doc-bd-a1/service-result bd-a1-image
```
3. Enter the Running Container
If you need to manually access the container at any point, use:
```bash
docker exec -it bd-a1-container bash
```
4. Load and Process the Dataset
Inside the running container, start the pipeline with:
```bash
python3 load.py /home/doc-bd-a1/dataset.csv
```
5. Copy Results to Local Machine
Once the pipeline has completed execution inside the container, run the following command from your host machine to transfer output files and stop the container:
```bash
bash final.sh
```
6. Verify Output Files
Check if the results have been successfully copied to service-result/:
```bash
ls service-result/
```
7. Push Docker Image to Docker Hub (Bonus)
To upload your image to Docker Hub, log in and push the image:
```bash
docker login
docker tag bd-a1-image H-Yahya2214/bd-a1-image:latest
docker push H-Yahya2214/bd-a1-image:latest
```
8. Push Project to GitHub
Initialize a Git repository and upload the project:
```bash
git init
git remote add origin https://github.com/H-Yahya2214/bd-a1-project
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```
Expected Output Files

- Preprocessed Data:
  - res_dpre.csv – Processed dataset after cleaning and transformation.

- Exploratory Data Analysis (EDA):
  - eda-in-1.txt, eda-in-2.txt, eda-in-3.txt – Key insights derived from the dataset.

- Visualization:
  - vis.png – Graphical representation of dataset trends.
 

- Clustering Output:
  - k.txt – Number of records in each of the K-Means clusters (k=3).
EDA Insights (from eda-in-1.txt, eda-in-2.txt, eda-in-3.txt)
•	Most common genre: Drama
•	Average IMDb rating: 7.94
•	Highest-grossing movie: Star Wars: Episode VII - The Force Awakens
Clustering Results (from k.txt)
•	Cluster 0: 360 movies
•	Cluster 1: 82 movies
•	Cluster 2: 272 movies

Our Repository & Container
  
Contributors
This project was completed as part of CSCI461 - Introduction to Big Data at Nile University, Spring 2025.

Team Members:
- [Sara Ahmed Talaat]
- [Habiba Yahya Ragaey]
- [Haneen Aly Abdelkader]
- [Engy Ahmed Saleh]
- [Ameena Yehia]
License
This project is for academic purposes only and follows Nile University’s guidelines on academic integrity.
