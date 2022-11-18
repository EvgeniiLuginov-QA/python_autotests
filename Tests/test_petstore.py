import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/108')
    assert response.status_code == 200

def test_namec_heck():
    response = requests.get('https://petstore.swagger.io/v2/pet/108')
    assert response.json()['name'] == 'Гаврюша'