import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_all_employees(client_fixture: APIClient):
    response = client_fixture.get('/api/all-employees')
    assert response.status_code == 200
