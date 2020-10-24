from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm, UserRegistrationForm

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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


#class RegisterView(CreateView):
#    form_class = UserCreationForm
#    success_url = 'login'
#    template_name = 'register.html'
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'form': user_form})


class MyLoginView(LoginView):
    redirect_authenticated_user = False
    template_name = "login.html"


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, что-то пошло не так :(. Запрашиваемая страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('ХЬЮСТОН, у нас проблемы... с сервером :(')
