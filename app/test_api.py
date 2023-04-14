from fastapi.testclient import TestClient
from .api import app

client = TestClient(app)


def test_get_data():
    url = "https://instagram.en.aptoide.com/app"
    response = client.get(f"get_url?url={url}")
    response_json = response.json()

    # test response status_code
    assert response.status_code == 200
    # test name: Instagram
    assert response_json.get("App's name", "") == "Instagram"
    # test version: 279.0.0.0.28
    # assert response_json.get("App's version", '') == "279.0.0.0.28"
    # test number of downloads: 115M
    assert response_json.get("Number of downloads") == "115M"


def test_get_invalid_url():
    url = "https://invalid.en.aptoide.com/app"
    response = client.get(f"get_url?url={url}")

    # test response status_code
    assert response.status_code == 400

    # test response_json
    assert response.json() == {}
