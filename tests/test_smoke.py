from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_app_starts():
    """
    Nuclear Smoke Test:
    If this passes, the app installed correctly and imports are working.
    """
    response = client.get("/")
    # We accept 200 (OK) or 404 (Not Found) or 405 (Method Not Allowed)
    # as long as it's not 500 (Server Error)
    assert response.status_code != 500
