import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


# get-all-employees requires nothing

def test_get_all_employees(client_fixture: APIClient):
    response = client_fixture.get('/api/all-employees')
    assert response.status_code == 200
    print(len(response.json()))


# get-all-employees-full requires auth

@pytest.mark.xfail
def test_get_all_employees_full_details(client_fixture: APIClient):
    response = client_fixture.get('/api/all-employees-full')
    assert response.status_code == 200


def test_get_all_employees_full_details_nonadmin(client_fixture: APIClient,
        nonadmin_token_fixture):
    response = client_fixture.get('/api/all-employees-full')
    assert response.status_code == 200


def test_get_all_employees_full_details_admin(client_fixture: APIClient,
        admin_token_fixture):
    response = client_fixture.get('/api/all-employees-full')
    assert response.status_code == 200
    print(len(response.json()))


# list-all-companies requires being an admin

@pytest.mark.xfail
def test_list_all_companies(client_fixture: APIClient):
    response = client_fixture.get('/api/all-companies')
    assert response.status_code == 200


@pytest.mark.xfail
def test_list_all_companies_nonadmin(client_fixture: APIClient,
        nonadmin_token_fixture):
    response = client_fixture.get('/api/all-companies')
    assert response.status_code == 200


def test_list_all_companies_admin(client_fixture: APIClient,
        admin_token_fixture):
    response = client_fixture.get('/api/all-companies')
    assert response.status_code == 200
    print(len(response.json()))


# get-all-banks requires being an admin

@pytest.mark.xfail
def test_get_all_banks(client_fixture: APIClient):
    response = client_fixture.get('/api/all-banks')
    assert response.status_code == 200


@pytest.mark.xfail
def test_get_all_banks_nonadmin(client_fixture: APIClient,
        nonadmin_token_fixture):
    response = client_fixture.get('/api/all-banks')
    assert response.status_code == 200


def test_get_all_banks_admin(client_fixture: APIClient,
        admin_token_fixture):
    response = client_fixture.get('/api/all-banks')
    assert response.status_code == 200
    print(len(response.json()))
