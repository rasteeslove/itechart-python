from rest_framework import serializers
from companymgmt.management import models


class DBRecordSerializer(serializers.Serializer):
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()


class CompanySerializer(DBRecordSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    website = serializers.URLField(max_length=30)
    email = serializers.EmailField(max_length=30)
    postcode = serializers.CharField(max_length=10)
    logo = serializers.ImageField()


class EmployeeSerializer(DBRecordSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    job_position = serializers.CharField(max_length=30)
    is_manager = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    phone_number = serializers.CharField(max_length=15)
    company = serializers.PrimaryKeyRelatedField(many=True)


class PersonalDataSerializer(DBRecordSerializer):
    id = serializers.IntegerField(read_only=True)
    birth_date = serializers.DateField()
    address = serializers.CharField(max_length=60)
    salary = serializers.DecimalField(max_digits=6, decimal_places=2)
    employee = serializers.PrimaryKeyRelatedField()


class BankSerializer(DBRecordSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    website = serializers.URLField(max_length=30)
    email = serializers.EmailField(max_length=30)
    company = serializers.PrimaryKeyRelatedField(many=True)
