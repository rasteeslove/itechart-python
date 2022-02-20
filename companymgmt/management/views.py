from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from management.models import Company, Employee, Bank
from management.serializers import CompanySerializer, EmployeeSerializer, BankSerializer


class GetAllEmployees(APIView):
    """
    A view to get all info about all employees.
    """
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class ListAllCompanies(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


@api_view()
def get_all_banks(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)