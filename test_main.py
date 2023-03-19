from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "sql_app v1.0"}

def test_create_user():
    response = client.get("/read_user/1")
    if response.status_code != 200:
        response = client.put("/create_user/", content='{ "first_name": "root", "last_name": "root" }', headers={"accept": "application/json", "Content-Type": "application/json"})
        assert response.status_code == 200
        assert response.json()["first_name"] == "root"
        assert response.json()["last_name"] == "root"
    else:
        if (response.json()["first_name"] != "root") | (response.json()["last_name"] != "root"):
            response = client.put("/update_user/", content='{ "first_name": "root", "last_name": "root", "id": 1 }', headers={"accept": "application/json", "Content-Type": "application/json"})
            assert response.status_code == 200
            assert response.json()["first_name"] == "root"
            assert response.json()["last_name"] == "root"

def test_update_user():
    response = client.put("/update_user/", content='{ "first_name": "root", "last_name": "root", "id": 1 }', headers={"accept": "application/json", "Content-Type": "application/json"})
    assert response.status_code == 200

def test_read_users():
    response = client.get("/read_users/")
    assert response.status_code == 200

def test_reade_user():
    response = client.get("/read_user/1")
    assert response.status_code == 200
    assert response.json()["first_name"] == "root"
    assert response.json()["last_name"] == "root"
