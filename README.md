Olivetti Faces Project

In this project, I implemented a complete MLOps workflow — from training a machine-learning model to deploying it with Docker, Kubernetes, and CI/CD.

Project Overview
I trained a face-recognition model using the Olivetti Faces dataset.
After training, I built a Flask API, containerized it using Docker, deployed it on Kubernetes, and automated testing using GitHub Actions.

What I Did
Trained the model in train.py
Created an API in app.py
Tested prediction using test.py
Built & pushed Docker image: shivani76/mlops_major

Deployed on Kubernetes using deployment.yaml
Added CI pipeline in .github/workflows/ci.yml

How to Run
Train the model: python train.py

Run Flask API: python app.py

Build Docker image:
docker build -t mlops_major .
docker push shivani76/mlops_major

Deploy on Kubernetes: kubectl apply -f deployment.yaml

Conclusion
This project helped me understand how ML models are developed, packaged, deployed, and automated in real MLOps pipelines.
