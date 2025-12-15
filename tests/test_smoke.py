from fastapi.testclient import TestClient
from app.main import app  # This import works only if PYTHONPATH is set correctly

client = TestClient(app)

def test_app_starts():
    """
    Nuclear Smoke Test:
    Verifies the app starts without crashing.
    """
    response = client.get("/")
    # We expect 200 (OK) but getting anything other than 500 means it started
    assert response.status_code != 500
