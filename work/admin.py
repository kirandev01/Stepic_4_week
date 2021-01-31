from django.contrib import admin
from .models import Company, Vacancy, Speciality, Application

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class Application(admin.ModelAdmin):
    list_filter = ('vacancy', 'user')

