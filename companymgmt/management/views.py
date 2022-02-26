from django.db.models import F
import json
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from management.models import Company, Employee, Bank, PersonalData
from management.serializers import CompanySerializer, EmployeeSerializer, BankSerializer, EmployeeFullDetailsSerializer
from management.decorators import allow_admins_only


class GetAllEmployees(APIView):
    """
    A view to get info about all employees, personal data excluded.
    """
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class GetAllEmployeesFullDetails(APIView):
    """
    A view to get info about all employees, personal data included.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeFullDetailsSerializer(employees, many=True)
        return Response(serializer.data)


class ListAllCompanies(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


@api_view()
@allow_admins_only
def get_all_banks(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_date_company(request):
    """
    Take two dates as arguments - A and B, A < B.
    Return a company that was created in a given date period
    and has the most recent update date that does not exceed B.
    """


@api_view(['POST'])
def salary_birthday_increase(request):
    """
    Take number and date as arguments.
    Increase salary by the number for all employees
    that have the date as their birthday.
    """
    birth_date_arg = request.data.get('birth_date')
    salary_increase_arg = request.data.get('salary_increase')
    personal_data_objects = PersonalData.objects.filter(
                                birth_date=birth_date_arg)
    personal_data_objects.update(salary=F('salary')+
                                salary_increase_arg)
    return Response()


@api_view(['POST'])
def create_companies(request):
    """
    Take any number of company data and create the companies.
    """
    for company_data in request.data.get('companies_data'):
        Company(**company_data).save()
    return Response()


@api_view(['GET'])
def get_newest_employees(request):
    """
    Return the last created employee for each company.
    """
    companies = Company.objects.all().iterator()
    employees = []
    for company in companies:
        employees.append(Employee.objects
            .filter(company=company.id)
            .latest('created'))
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
