# Use Ubuntu as the base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && python3 -m venv /home/venv \
    && /home/venv/bin/pip install --no-cache-dir pandas numpy seaborn matplotlib scikit-learn scipy \
    && apt-get clean

# Activate the virtual environment inside the container
ENV PATH="/home/venv/bin:$PATH"

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1

# Copy the dataset into the container
COPY imdb_top_1000.csv /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1

# Start a Bash shell when the container runs
CMD ["/bin/bash"]
