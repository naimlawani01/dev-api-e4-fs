import pytest
from main import app
from fastapi.testclient import TestClient
from models.Driver import Driver
from database.firebase import authSession
from tests.conftest import auth_headers, driver_id

client =  TestClient(app)

def test_create_an_account(valid_user_data, cleanup):
    response = client.post("/api/auth/signup", json=valid_user_data)
    assert response.status_code == 201
    assert "message" in response.json()

def test_create_an_account_duplicate_email(valid_user_data, cleanup):
    # Create a user with the same email to simulate a duplicate email error
    response = client.post("/api/auth/signup", json=valid_user_data)
    assert response.status_code == 409
    assert "detail" in response.json()

def test_create_swagger_token(valid_user_data, cleanup):
    response = client.post("/api/auth/login", data={"username": valid_user_data["email"], "password": valid_user_data["password"]})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()

def test_create_swagger_token_invalid_credentials():
    # Test with invalid credentials
    response = client.post("/api/auth/login", data={"username": "invalid@example.com", "password": "invalidpassword"})
    assert response.status_code == 401

def test_secure_endpoint(auth_token, cleanup):
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert "idToken" in response.json()