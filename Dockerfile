FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && python3 -m venv /home/venv \
    && /home/venv/bin/pip install --no-cache-dir pandas numpy seaborn matplotlib scikit-learn scipy \
    && apt-get clean

ENV PATH="/home/venv/bin:$PATH"

RUN mkdir -p /home/doc-bd-a1

COPY imdb_top_1000.csv /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1

CMD ["/bin/bash"]
