from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "online", "version": "0.1.0"}

def test_read_containers():
    resp = client.get("/containers")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    
def test_read_containers_stats():
    resp = client.get("/containers/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    
    # Pokud máš aspoň jeden běžící kontejner, zkontroluj strukturu prvního z nich
    if len(data) > 0:
        assert "name" in data[0]
        assert "mem_usage_mb" in data[0]