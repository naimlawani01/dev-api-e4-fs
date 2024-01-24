import pytest
from main import app
from fastapi.testclient import TestClient


client =  TestClient(app)

def test_docs():
    res= client.get("/docs")
    assert res.status_code == 200


# Ecrire test /redocs
    
def test_redoc():
    res = client.get("/redoc")
    assert res.status_code == 200