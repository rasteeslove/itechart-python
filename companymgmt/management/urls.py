from django.urls import path
from management.views import (ListAllCompanies,
                              GetAllEmployees,
                              GetAllEmployeesFullDetails,
                              get_all_banks,
                              get_date_company,
                              salary_birthday_increase,
                              create_companies,
                              get_newest_employees)


mgmt_urlpatterns = [
    path('all-companies', ListAllCompanies.as_view()),
    path('all-employees', GetAllEmployees.as_view()),
    path('all-employees-full', GetAllEmployeesFullDetails.as_view()),
    path('all-banks', get_all_banks),

    # orm task:
    path('date-company', get_date_company),
    path('salary-birthday-increase', salary_birthday_increase),
    path('create-companies', create_companies),
    path('newest-employees', get_newest_employees),
]
