import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_get_date_company_01(client_fixture: APIClient):
    response = client_fixture.get('/api/date-company',
        {'date_a': '2022-01-05', 'date_b': '2022-01-15'})
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == 'A'


def test_get_date_company_02(client_fixture: APIClient):
    response = client_fixture.get('/api/date-company',
        {'date_a': '2022-01-05', 'date_b': '2022-01-25'})
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == 'B'


def test_get_date_company_03(client_fixture: APIClient):
    response = client_fixture.get('/api/date-company',
        {'date_a': '2022-02-05', 'date_b': '2022-02-15'})
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == 'F'


def test_get_date_company_04(client_fixture: APIClient):
    response = client_fixture.get('/api/date-company',
        {'date_a': '2022-02-05', 'date_b': '2022-02-25'})
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == 'D'


def test_get_date_company_05(client_fixture: APIClient):
    response = client_fixture.get('/api/date-company',
        {'date_a': '2022-01-05', 'date_b': '2022-03-15'})
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == 'C'


def test_get_date_company_06(client_fixture: APIClient):
    response = client_fixture.get('/api/date-company',
        {'date_a': '2022-01-15', 'date_b': '2022-03-15'})
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == 'D'


# TODO: test in nonsensical range
# TODO: test in same-day range
# TODO: test in empty range (i.e. in range
# for which the view will yield nothing)
