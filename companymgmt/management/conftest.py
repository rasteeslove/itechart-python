"""
The home for fixtures.
"""

import pytest
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def client_fixture():
    client = APIClient()
    return client
