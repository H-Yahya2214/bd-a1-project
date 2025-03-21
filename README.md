Big Data Assignment 1 - Data Processing Pipeline
Project Overview
This project implements a data processing pipeline using Docker. The pipeline runs inside a container based on an Ubuntu image, where a dataset is processed through multiple steps:

Loading the dataset.

Preprocessing: Data cleaning, transformation, reduction, and discretization.

Exploratory Data Analysis (EDA): Extracting insights.

Visualization: Creating graphical representations.

Clustering using K-Means (k=3).

Copying results from the container to the local machine.

Features
Containerized Environment: Runs in an isolated Docker container for reproducibility.

Automated Pipeline: Data flows seamlessly from one step to the next without manual intervention.

Data Processing & Transformation: Includes cleaning, reducing, and structuring data for analysis.

Exploratory Data Analysis (EDA): Generates key insights from the dataset.

Visual Representation: Creates a visualization (vis.png).

Machine Learning with K-Means: Applies clustering with k=3.

Automatic Results Extraction: Copies output files from the container to the host machine.

Prerequisites
Before running the project, ensure you have the following installed:

Docker: Install Docker

Python 3.x: Installed inside the Docker container.

Dataset: A CSV file (e.g., imdb_top_1000.csv) to process.

Directory Structure
Copy
bd-a1/
│── Dockerfile                # Docker configuration file
│── imdb_top_1000.csv         # Example dataset
│── load.py                   # Script to load and clean data
│── dpre.py                   # Script for data preprocessing
│── eda.py                    # Script for exploratory data analysis
│── vis.py                    # Script for visualization
│── model.py                  # Script for K-Means clustering
│── final.sh                  # Script to copy results to the host machine
│── service-result/           # Directory to store output files
│── README.md                 # Project documentation
Execution Steps
1. Build the Docker Image
Run the following command in the project directory to build the Docker image:

bash
Copy
docker build -t bd-a1-image .
2. Run the Docker Container
Create and start a container while mounting the service-result directory to store results:

bash
Copy
docker run -it --name bd-a1-container -v $(pwd)/service-result:/home/doc-bd-a1/service-result bd-a1-image
3. Enter the Running Container (Optional)
If you need to manually access the container at any point, use:

bash
Copy
docker exec -it bd-a1-container bash
4. Load and Process the Dataset
Inside the running container, start the pipeline with:

bash
Copy
python3 load.py /home/doc-bd-a1/imdb_top_1000.csv
5. Copy Results to Local Machine
Once the pipeline has completed execution inside the container, run the following command from your host machine to transfer output files and stop the container:

bash
Copy
bash final.sh
6. Verify Output Files
Check if the results have been successfully copied to service-result/:

bash
Copy
ls service-result/
7. Push Docker Image to Docker Hub (Optional)
To upload your image to Docker Hub, log in and push the image:

bash
Copy
docker login
docker tag bd-a1-image H-Yahya2214/bd-a1-image:latest
docker push H-Yahya2214/bd-a1-image:latest
8. Push Project to GitHub (Optional)
Initialize a Git repository and upload the project:

bash
Copy
git init
git remote add origin https://github.com/H-Yahya2214/bd-a1-project
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
Expected Output Files
Preprocessed Data:

res_dpre.csv – Processed dataset after cleaning and transformation.

Exploratory Data Analysis (EDA):

eda-in-1.txt, eda-in-2.txt, eda-in-3.txt – Key insights derived from the dataset.

Visualization:

vis.png – Graphical representation of dataset trends.

Clustering Output:

k.txt – Number of records in each of the K-Means clusters (k=3).

EDA Insights (from eda-in-1.txt, eda-in-2.txt, eda-in-3.txt)
Most Common Genre: Drama

Average IMDb Rating: 7.94

Highest-Grossing Movie: Star Wars: Episode VII - The Force Awakens

Clustering Results (from k.txt)
Cluster 0: 360 movies

Cluster 1: 82 movies

Cluster 2: 272 movies

Contributors
This project was completed as part of CSCI461 - Introduction to Big Data at Nile University, Spring 2025.

Team Members:
[Sara Ahmed Talaat]

[Habiba Yahya Ragaey]

[Haneen Aly Abdelkader]

[Engy Ahmed Saleh]

[Ameena Yehia]

License
This project is for academic purposes only and follows Nile University’s guidelines on academic integrity.


