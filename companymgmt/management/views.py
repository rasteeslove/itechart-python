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
