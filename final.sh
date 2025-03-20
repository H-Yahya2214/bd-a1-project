#!/bin/bash

LOCAL_DIR="./service-result"

mkdir -p "$LOCAL_DIR"

docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv "$LOCAL_DIR/"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt "$LOCAL_DIR/"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt "$LOCAL_DIR/"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt "$LOCAL_DIR/"
docker cp bd-a1-container:/home/doc-bd-a1/vis.png "$LOCAL_DIR/"
docker cp bd-a1-container:/home/doc-bd-a1/k.txt "$LOCAL_DIR/"

docker stop bd-a1-container
