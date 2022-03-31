import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_get_all_employees(client_fixture: APIClient):
    response = client_fixture.get('/api/all-employees')
    assert response.status_code == 200
    print(response.json())


def test_get_all_employees_full_details(client_fixture: APIClient):
    response = client_fixture.get('/api/all-employees-full')
    assert response.status_code == 200
    print(response.json())


def test_list_all_companies(client_fixture: APIClient):
    response = client_fixture.get('/api/all-companies')
    assert response.status_code == 200
    print(response.json())


def test_get_all_banks(client_fixture: APIClient):
    response = client_fixture.get('/api/all-banks')
    assert response.status_code == 200
    print(response.json())
    