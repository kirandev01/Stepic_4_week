import os
import django
from data import specialties, companies, jobs
os.environ.setdefault('DJANGO_SETTINGS_MODULE','conf.settings')
django.setup()


from work.models import Company

def populate():
    for company in companies:
        Company.objects.create(name=company['title'])
        print(company['title'])


if __name__ == "__main__":
    populate()
