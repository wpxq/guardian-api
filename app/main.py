from fastapi import FastAPI
from app.services import get_docker_status, get_system_stats, get_detailed_stats

app = FastAPI(title="Guardian API", version="0.1.0")

@app.get("/health")
async def health_check():
    return {"status": "online", "version": "0.1.0"}

@app.get("/containers")
async def containers():
    return get_docker_status()

@app.get("/system")
async def system():
    return get_system_stats()

@app.get("/containers/stats")
async def container_status():
    return get_detailed_stats()