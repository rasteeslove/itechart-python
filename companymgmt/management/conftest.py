"""
The home for fixtures.
"""

import pytest
from rest_framework.test import APIClient
from django.core.management import call_command


@pytest.fixture(autouse=True, scope='session')
def setup_and_clear_database(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data_samples_for_testing/samples_1.json')


@pytest.fixture(autouse=True, scope='session')
def client_fixture():
    client = APIClient()
    return client


@pytest.fixture(autouse=False, scope='function')
@pytest.mark.django_db
def admin_token_fixture(client_fixture):
    response = client_fixture.post('/token/',
        {'username': 'krastsislau', 'password': '$def#p@ss'},
        format='json')
    assert response.status_code == 200
    access_token = response.data['access']

    client_fixture.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    yield

    client_fixture.credentials(HTTP_AUTHORIZATION='')


@pytest.fixture(autouse=False, scope='function')
def nonadmin_token_fixture(client_fixture):
    response = client_fixture.post('/token/',
        {'username': 'joe', 'password': 'wh@tever'},
        format='json')
    assert response.status_code == 200
    access_token = response.data['access']

    client_fixture.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    yield

    client_fixture.credentials(HTTP_AUTHORIZATION='')
