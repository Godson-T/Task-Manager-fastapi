from fastapi.testclient import TestClient
from main import app

client=TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    
def test_create_task_without_token():
    response = client.post(
        "/task",
        json={
            "title": "test",
            "description": "test desc",
            "completed": False
        }
    )

    assert response.status_code == 422
    
def test_create_task_with_valid_token():
    login_response = client.post(
    "/login",
    data={
        "username": "testuser3",
        "password": "testpass"
    }
    )

    print("LOGIN STATUS:", login_response.status_code)
    print("LOGIN RESPONSE:", login_response.json())

    token = login_response.json()["access_token"]