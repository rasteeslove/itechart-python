import pytest
from rest_framework.test import APIClient

from management.models import PersonalData


pytestmark = pytest.mark.django_db


def test_birthday_increase_01(client_fixture: APIClient):
    pdatas = PersonalData.objects.filter(birth_date='2000-10-10')
    old_salaries = [pdata.salary for pdata in pdatas]
    response = client_fixture.post('/api/salary-birthday-increase',
        {'birth_date': '2000-10-10', 'salary_increase': 10},
        format='json')
    assert response.status_code == 200
    pdatas = PersonalData.objects.filter(birth_date='2000-10-10')
    new_salaries = [pdata.salary for pdata in pdatas]
    for old, new in zip(old_salaries, new_salaries):
        assert new == old+10


def test_birthday_increase_02(client_fixture: APIClient):
    pdatas = PersonalData.objects.filter(birth_date='1995-02-02')
    old_salaries = [pdata.salary for pdata in pdatas]
    response = client_fixture.post('/api/salary-birthday-increase',
        {'birth_date': '1995-02-02', 'salary_increase': 100},
        format='json')
    assert response.status_code == 200
    pdatas = PersonalData.objects.filter(birth_date='1995-02-02')
    new_salaries = [pdata.salary for pdata in pdatas]
    for old, new in zip(old_salaries, new_salaries):
        assert new == old+100


def test_birthday_increase_03(client_fixture: APIClient):
    pdatas = PersonalData.objects.filter(birth_date='1990-06-06')
    old_salaries = [pdata.salary for pdata in pdatas]
    response = client_fixture.post('/api/salary-birthday-increase',
        {'birth_date': '1990-06-06', 'salary_increase': 1000},
        format='json')
    assert response.status_code == 200
    pdatas = PersonalData.objects.filter(birth_date='1990-06-06')
    new_salaries = [pdata.salary for pdata in pdatas]
    for old, new in zip(old_salaries, new_salaries):
        assert new == old+1000


# TODO: test nonsensical input
# TODO: test unmatched input
# TODO: test negative salary 'increase'
