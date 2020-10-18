import os
import django
from data import specialties, companies, jobs
os.environ.setdefault('DJANGO_SETTINGS_MODULE','conf.settings')
django.setup()


from work.models import Speciality

def populate():
    for specialty in specialties:
       # dict = specialty.items()
        Speciality.objects.create(code=specialty['code'], title=specialty['title'])
        print(specialty['title'])


if __name__ == "__main__":
    populate()