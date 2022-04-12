import pytest
from rest_framework.test import APIClient

from management.models import PersonalData


pytestmark = pytest.mark.django_db


# TODO: test nonsensical input
# TODO: test unmatched input
# TODO: test negative salary 'increase'
test_cases = [
    ('2000-10-10', 10),
    ('1995-02-02', 100),
    ('1990-06-06', 1000),
]


@pytest.mark.parametrize('date, increase', test_cases)
def test_birthday_increase(client_fixture: APIClient, date, increase):
    pdatas = PersonalData.objects.filter(birth_date=date)
    old_salaries = [pdata.salary for pdata in pdatas]
    response = client_fixture.post('/api/salary-birthday-increase',
                                   {
                                       'birth_date': date,
                                       'salary_increase': increase,
                                   },
                                   format='json')
    assert response.status_code == 200
    pdatas = PersonalData.objects.filter(birth_date=date)
    new_salaries = [pdata.salary for pdata in pdatas]
    for old, new in zip(old_salaries, new_salaries):
        assert new == old+increase
