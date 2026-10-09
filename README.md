# Student REST API on Kubernetes

CMPE-272: Enterprise Software Platforms

## Student Information

- Student name: Apoorva Pramod Mahajan
- Operating system: macOS
- Kubernetes environment: Docker Desktop Kubernetes

## Project Description

This project implements a Flask REST API for managing university students. The API is packaged as a Docker image and deployed to Kubernetes with two replicas.

## Project Files

```text
student-api/
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── README.md
└── screenshots/
```

## Installations

- Python 3.11 or later
- Flask 3.0.0
- Docker Desktop
- Kubernetes kubectl
- Docker Desktop Kubernetes cluster

## Run Locally

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

The local API listens on `http://localhost:5000`.

## Build and Run the Docker Image

```bash
docker build -t student-api:1.0 .
docker run --rm -p 5000:5000 student-api:1.0
```

## Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get deployments
kubectl get pods
kubectl get services
```

The Deployment runs two replicas. The readiness probe checks `GET /health` on port `5000`.

Forward the Service port to localhost:

```bash
kubectl port-forward service/student-api-service 8080:80
```

The Kubernetes API is then available at `http://localhost:8080`.

## API Endpoints

| Method | Endpoint | Expected result |
|---|---|---|
| GET | `/` | Welcome message, HTTP 200 |
| GET | `/health` | Health status, HTTP 200 |
| GET | `/students` | All students, HTTP 200 |
| GET | `/students/<id>` | One student or HTTP 404 |
| POST | `/students` | Creates a student, HTTP 201 |
| DELETE | `/students/<id>` | Deletes a student or HTTP 404 |

## Required Test Commands

```bash
curl -i http://localhost:8080/
curl -i http://localhost:8080/health
curl -i http://localhost:8080/students
curl -i http://localhost:8080/students/2

curl -i -X POST http://localhost:8080/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Maya Smith","major":"Data Science"}'

curl -i -X DELETE http://localhost:8080/students/5
curl -i http://localhost:8080/students/99

curl -i -X POST http://localhost:8080/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Incomplete Student"}'
```

## Test Results

- Welcome endpoint: PASS - HTTP 200
- Health endpoint: PASS - HTTP 200
- Initial five students: PASS
- Retrieve student ID 2: PASS - HTTP 200
- Create student ID 6: PASS - HTTP 201
- Delete student ID 5: PASS - HTTP 200
- Invalid student ID 99: PASS - HTTP 404
- Invalid POST request: PASS - HTTP 400

## Screenshots

The required screenshots are stored in the `screenshots/` folder:

- `01-docker-build.png`
- `02-deployment.png`
- `03-pods-ready.png`
- `04-get-services.png`
- `05-Test1.png`
- `06-Text2-Health.png`
- `07-Test3-Students.png`
- `08-Test4-retrieve.png`
- `09-test5-addStudent.png`
- `10-test6-delete.png`
- `11-test7-invalidStudent.png`
- `12-test8-invalidPost.png`

## Assumptions and Limitations
- The Kubernetes Deployment uses two replicas with the local Docker image `student-api:1.0`.
- No persistent database is used.