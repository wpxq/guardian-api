![Tests](https://github.com/wpxq/guardian-api/actions/workflows/tests.yml/badge.svg)

# Guardian API

A lightweight, production-ready FastAPI backend designed for Docker infrastructure monitoring and real-time container observability.

## Key Features

- **Container Monitoring**: Lists all running and stopped containers using Docker SDK.
- **Live Statistics**: Real-time CPU and RAM usage metrics for each container.
- **Automated Testing**: Robust test suite using `pytest` with high coverage.
- **Containerized Workflow**: Fully dockerized environment with `docker-compose` support.
- **CI/CD Ready**: Integrated GitHub Actions for automated testing on every push.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Runtime**: Python 3.11+
- **Infrastructure**: Docker & Docker Compose
- **Testing**: Pytest & HTTPX
- **Server**: Uvicorn

## Quick Start

### Prerequisites
- Docker and Docker Compose installed on your system.
- (Optional) Python 3.11+ for local development.

### Running with Docker Compose (Recommended)
The easiest way to get the API up and running:

```bash
git clone https://github.com/wpxq/guardian-api
cd guardian-api
```
```bash
docker compose up -d
```
The API will be available at `http://localhost:8080`

## API Endpoints
* `GET /health`: Check if the API is alive
* `GET /containers`: List all containers on the host
* `GET /containers/stats`: Get detailed RAM and CPU metrics
* `GET /docs`: INteractive Swagger UI documentation

## Testing
To run the automated test suite locally:
```bash
PYTHONPATH=. pytest
```
or (if no issues)
```bash
pytest
```
## Deployment
The project includes a `Dockerfile` for easy deployment. Note that the container requires
access to the Docker socket (`/var/run/docker.sock`) to communicate with the Docker
daemon
