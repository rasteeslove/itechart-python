import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_get_newest_employees(client_fixture: APIClient):
    response = client_fixture.get('/api/newest-employees')
    assert response.status_code == 200
    newest_employees = response.json()
    assert len(newest_employees) == 6
    ids = [e['id'] for e in newest_employees]
    assert ids == [7, 8, 9, 10, 11, 12]
