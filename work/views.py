from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.db.models import Count

from work.models import Company, Speciality, Vacancy


def main_view(request):
    title = 'Джуманджи'
    offers = Speciality.objects.annotate(number_of_vacancies=Count('vacancies__id'))
    offers_of_companies = Company.objects.annotate(number_of_vacancies=Count('vacancies__id'))
    return render(request, 'index.html', {'title': title, 'offers_of_companies': offers_of_companies, 'offers': offers})


def vacancies(request):
    title = 'Вакансии | Джуманджи'
    head_title = 'Все вакансии'
    vacancies = Vacancy.objects.all()
    number_of_vacancies = calculate_vacancies(vacancies)
    return render(request, 'vacancies.html', {'title': title, 'head_title': head_title,
                                              'number_of_vacancies': number_of_vacancies, 'vacancies': vacancies})


def speciality(request, speciality):
    title = 'Вакансии | Джуманджи'
    speciality = Speciality.objects.get(code=speciality)
    head_title = speciality.title
    vacancies = Vacancy.objects.filter(speciality=speciality)
    number_of_vacancies = calculate_vacancies(vacancies)
    return render(request, 'vacancies.html', {'title': title, 'head_title': head_title,
                                              'number_of_vacancies': number_of_vacancies, 'vacancies': vacancies})


def calculate_vacancies(vacancies):
    number_of_vacancies = vacancies.count
    if number_of_vacancies == 0:
        number_of_vacancies = 'Извините, вакансии закончились. Приходите завтра.'
    return number_of_vacancies


def vacancy(request, vacancy_id):
    title = 'Вакансия | Джуманджи'
    vacancy = Vacancy.objects.get(id=vacancy_id)
    company = vacancy.company
    return render(request, 'vacancy.html', {'title': title, 'vacancy': vacancy, 'company': company})


def company(request, company_id):
    title = 'Компания | Джуманджи'
    company = Company.objects.get(id=company_id)
    head_title = company.name
    vacancies = Vacancy.objects.filter(company=company)
    number_of_vacancies = calculate_vacancies(vacancies)
    return render(request, 'vacancies.html', {'title': title, 'head_title': head_title,
                                              'number_of_vacancies': number_of_vacancies, 'vacancies': vacancies})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, что-то пошло не так :(. Запрашиваемая страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('ХЬЮСТОН, у нас проблемы... с сервером :(')
