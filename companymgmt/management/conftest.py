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
