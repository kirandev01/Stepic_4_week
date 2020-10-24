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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)