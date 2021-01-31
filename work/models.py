from django.db import models
from django.contrib.auth import get_user_model
from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Speciality(models.Model):
    code = models.SlugField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return f'{self.title}'


class Company(models.Model):
    name = models.CharField('Название компании', max_length=100)
    location = models.CharField('География', max_length=50)
    logo = models.ImageField('Логотип', upload_to=MEDIA_COMPANY_IMAGE_DIR, blank=True, )
    employee_count = models.IntegerField('Количество человек в компании')
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                 related_name='company')
    description = models.TextField('Информация о компании')

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skils = models.CharField(max_length=200)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Application(models.Model):
    written_username = models.CharField('Вас зовут', max_length=100)
    writtem_phone = models.CharField('Ваш телефон', max_length=12)
    written_cover_letter = models.TextField('Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return f'{self.written_username}'
