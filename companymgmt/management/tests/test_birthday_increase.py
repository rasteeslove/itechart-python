import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_birthday_increase_01(client_fixture: APIClient):
    response = client_fixture.post('/api/salary-birthday-increase',
        {'birth_date': '2000-10-10', 'salary_increase': 10},
        format='json')
    assert response.status_code == 200


def test_birthday_increase_02(client_fixture: APIClient):
    response = client_fixture.post('/api/salary-birthday-increase',
        {'birth_date': '1995-02-02', 'salary_increase': 100},
        format='json')
    assert response.status_code == 200


def test_birthday_increase_03(client_fixture: APIClient):
    response = client_fixture.post('/api/salary-birthday-increase',
        {'birth_date': '1990-06-06', 'salary_increase': 1000},
        format='json')
    assert response.status_code == 200


# TODO: test nonsensical input
# TODO: test unmatched input
# TODO: test negative salary 'increase'
