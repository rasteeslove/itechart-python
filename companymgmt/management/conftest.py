"""
The home for fixtures.
"""

import pytest
from rest_framework.test import APIClient
from management.models import Employee, Company


@pytest.fixture(autouse=True, scope='function')
@pytest.mark.django_db
def setup_and_clear_database():
    test_company = Company(
        name='Apple Company',
        website='apple.com',
        email='apple@gmail.com',
        postcode='202020',
    )
    test_company.save()
    test_employee = Employee(
        first_name='Bob',
        last_name='Dylan',
        job_position='Worker',
        is_manager=True,
        is_admin=False,
        phone_number='111',
        company=Company.objects.filter(name='Apple Company').first()
    )
    test_employee.save()

    yield

    Employee.objects.filter(last_name='Dylan').delete()
    Company.objects.filter(name='Apple Company').delete()


@pytest.fixture(autouse=True, scope='session')
def client_fixture():
    client = APIClient()
    return client
