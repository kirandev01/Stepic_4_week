import os
import datetime
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()  # Всякие Django штуки импортим после сетапа


from work.models import Company, Speciality, Vacancy
from data import specialties, companies, jobs


if __name__ == '__main__':
    Speciality.objects.all().delete()
    Company.objects.all().delete()
    Vacancy.objects.all().delete()

    for speciality in specialties:
        Speciality.objects.create(
            code=speciality['code'],
            title=speciality['title'],
        )

    for company in companies:
        Company.objects.create(
            name=company['title'],
            logo='',
            employee_count=1,
        )

    for vacancy in jobs:
        Vacancy.objects.create(
            title=vacancy['title'],
            speciality=Speciality.objects.get(code=vacancy['cat']),
            company=Company.objects.get(name=vacancy['company']),
            description=vacancy['desc'],
            salary_min=vacancy['salary_from'],
            salary_max=vacancy['salary_to'],
            published_at=datetime.date.fromisoformat(vacancy['posted']),
        )
