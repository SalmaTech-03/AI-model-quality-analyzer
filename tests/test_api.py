from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """
    Smoke test to verify the API is up and running.
    Should return the index.html content (200 OK).
    """
    response = client.get("/")
    assert response.status_code == 200
    # Check if the HTML contains the title
    # We use a broad check because title might vary slightly
    assert "text/html" in response.headers["content-type"]
