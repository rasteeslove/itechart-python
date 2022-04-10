import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_get_newest_employees(client_fixture: APIClient):
    pass # TODO: ...
