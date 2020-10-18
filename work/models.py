from django.db import models


class Speciality(models.Model):
    code = models.SlugField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    logo = models.CharField(max_length=100)
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skils = models.CharField(max_length=200)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now=True)
