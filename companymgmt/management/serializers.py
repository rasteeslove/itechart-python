from rest_framework import serializers
from management.models import Company, Employee, Bank


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeFullDetailsSerializer(serializers.ModelSerializer):
    """
    The serializer to be used to get all data about an employee
    in one JSON-layer (combine Employee instance data and
    composition-related PersonalData).
    """
    birth_date = serializers.DateField(source='personal_data.birth_date')
    address = serializers.CharField(max_length=60, source='personal_data.address')
    salary = serializers.DecimalField(max_digits=6, decimal_places=2,
                                      source='personal_data.salary')

    class Meta:
        model = Employee
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
