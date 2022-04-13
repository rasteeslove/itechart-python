from django.db import models


class DBRecord(models.Model):
    """
    To store db objects' metadata (i.e., creation datetime
    and last update datetime)
    """
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(DBRecord):
    name: models.CharField = models.CharField(max_length=30)
    website: models.URLField = models.URLField(max_length=30)
    email: models.EmailField = models.EmailField(max_length=30)
    postcode: models.CharField = models.CharField(max_length=10)
    logo: models.ImageField = models.ImageField(upload_to='logos', blank=True)

    def __str__(self) -> str:
        return self.name


class Employee(DBRecord):
    """
    Represents not as much as an employee themself,
    but rather the fact of employment.
    Hence if changing employer, must be reinstantiated.
    """
    first_name: models.CharField = models.CharField(max_length=30)
    last_name: models.CharField = models.CharField(max_length=30)
    job_position: models.CharField = models.CharField(max_length=30)
    is_manager: models.BooleanField = models.BooleanField(default=False)
    is_admin: models.BooleanField = models.BooleanField(default=False)
    phone_number: models.CharField = models.CharField(max_length=15)
    company: models.ForeignKey = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,  # if company is deleted,
                                   # so are its employees
        related_name='employee'
    )

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class PersonalData(DBRecord):
    birth_date: models.DateField = models.DateField()
    address: models.CharField = models.CharField(max_length=60)
    salary: models.DecimalField = models.DecimalField(max_digits=6,
                                                      decimal_places=2)
    employee: models.OneToOneField = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,  # if employee is deleted,
                                   # personal data should be too
        related_name='personal_data'
    )

    def __str__(self) -> str:
        return f'{self.employee}\'s data'


class Bank(DBRecord):
    name: models.CharField = models.CharField(max_length=30)
    website: models.URLField = models.URLField(max_length=30)
    email: models.EmailField = models.EmailField(max_length=30)
    company: models.ManyToManyField = models.ManyToManyField(
        Company,
        related_name='bank'
    )

    def __str__(self) -> str:
        return self.name
