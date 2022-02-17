from logging import captureWarnings
from rest_framework import serializers
from companymgmt.management import models


class DBRecordSerializer(serializers.Serializer):
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    website = serializers.URLField(max_length=30)
    email = serializers.EmailField(max_length=30)
    postcode = serializers.CharField(max_length=10) # tmp workaround
    logo = serializers.ImageField()


class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    job_position = serializers.CharField(max_length=30)
    is_manager = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    phone_number = serializers.CharField(max_length=15) # tmp workaround
    company = serializers.PrimaryKeyRelatedField(many=True)


class PersonalDataSerializer(serializers.Serializer):
    birth_date = serializers.DateField()
    address = serializers.CharField(max_length=60) # tmp workaround (TextField maybe ?)
    salary = serializers.DecimalField(max_digits=6, decimal_places=2)
    employee = serializers.PrimaryKeyRelatedField()


class BankSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    website = serializers.URLField(max_length=30)
    email = serializers.EmailField(max_length=30)
    company = serializers.PrimaryKeyRelatedField(many=True)
