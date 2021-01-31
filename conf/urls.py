"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from work import views

handler404 = views.custom_handler404
handler500 = views.custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('vacancies/', views.vacancies),
    path('vacancies/cat/<str:speciality>', views.speciality),
    path('vacancies/<int:vacancy_id>', views.vacancy),
    path('companies/<int:company_id>', views.company),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('vacancies/<int:pk>/send/', views.send, name='send'),
    path('mycompany/', views.mycompany, name='mycompany'),
    path('mycompany/<int:pk>/', views.company_edit, name='company_edit'),
    path('mycompany/new/', views.company_new, name='company_new'),
    path('mycompany/vacancies/', views.vacancy_list, name='vacancy_list'),
    path('mycompany/vacancies/new/', views.vacancy_new, name='vacancy_new'),
    path('mycompany/vacancies/<int:pk>/', views.vacancy_edit, name='vacancy_edit')
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
