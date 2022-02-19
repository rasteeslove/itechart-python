from rest_framework import serializers
from management.models import Company, Employee, PersonalData, Bank


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'email', 'postcode']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'job_position',
                  'is_manager', 'is_admin', 'phone_number', 'company']


class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ['id', 'birth_date', 'address', 'salary', 'employee']


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'website', 'email', 'company']
