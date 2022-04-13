import pytest
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


# TODO: test nonsensical input
# TODO: test unmatched input
# TODO: test in same-day range
test_cases = [
    ({'date_a': '2022-01-05', 'date_b': '2022-01-15'}, 'A'),
    ({'date_a': '2022-01-05', 'date_b': '2022-01-25'}, 'B'),
    ({'date_a': '2022-02-05', 'date_b': '2022-02-15'}, 'F'),
    ({'date_a': '2022-02-05', 'date_b': '2022-02-25'}, 'D'),
    ({'date_a': '2022-01-05', 'date_b': '2022-03-15'}, 'C'),
    ({'date_a': '2022-01-15', 'date_b': '2022-03-15'}, 'D'),
]


@pytest.mark.parametrize('dates, res_company_name', test_cases)
def test_get_date_company(client_fixture: APIClient,
                          dates: dict,
                          res_company_name: str) -> None:
    response = client_fixture.get('/api/date-company', dates)
    assert response.status_code == 200
    company = response.json()
    assert company['name'] == res_company_name
