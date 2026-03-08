from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_chat_validation_error():
    # Sending empty body should fail validation
    response = client.post("/chat/generate", json={})
    assert response.status_code == 422
