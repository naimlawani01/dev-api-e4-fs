import pytest
from firebase_admin import auth
from fastapi.testclient import TestClient
from main import app
from database.firebase import authSession

@pytest.fixture
def auth_token():
    email = "test.auth@gmail.com"
    password = "password123"
    user = auth.create_user(
        email=email,
        password=password
    )
    token = authSession.sign_in_with_email_and_password(email=email, password=password)['idToken']
    return token

@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    #Nettoyer le directory une fois fini
    def remove_test_users():
        users = auth.list_users().iterate_all()
        for user in users:
            if user.email.startswith("test"):
                auth.delete_user(user.uid)
    request.addfinalizer(remove_test_users)
@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}
