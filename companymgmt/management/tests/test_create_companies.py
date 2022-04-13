import pytest
from rest_framework.test import APIClient

from management.models import Company


pytestmark = pytest.mark.django_db


sample_01 = [
    {
        'name': 'TestCompany01',
        'website': 'test.com',
        'email': 'test@test.com',
        'postcode': '111111',
    },
    {
        'name': 'TestCompany02',
        'website': 'test.com',
        'email': 'test@test.com',
        'postcode': '111111',
    }
]


def test_create_companies(client_fixture: APIClient) -> None:
    old_companies_number = len(Company.objects.all())
    response = client_fixture.post('/api/create-companies',
                                   {'companies_data': sample_01},
                                   format='json')
    assert response.status_code == 200
    new_companies_number = len(Company.objects.all())
    assert new_companies_number == old_companies_number+2
