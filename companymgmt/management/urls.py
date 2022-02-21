from django.urls import path
from management.views import ListAllCompanies, GetAllEmployees, GetAllEmployeesFullDetails, get_all_banks


mgmt_urlpatterns = [
    path('all-companies', ListAllCompanies.as_view()),
    path('all-employees', GetAllEmployees.as_view()),
    path('all-employees-full', GetAllEmployeesFullDetails.as_view()),
    path('all-banks', get_all_banks),
]
