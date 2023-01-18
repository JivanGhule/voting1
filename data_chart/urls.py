"""data_chart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views

# from app.views import GeneratePdf
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='home'),
    path('registration/', views.Registration,name='registration'),
    path('login/', views.Login,name='login'),
    path('vote/', views.Vote,name='vote'),
    path('result/', views.Result,name='result'),
    path('pdf/', views.pdf,name='pdf'),
    path('download_id/', views.download_id,name='download_id'),
    path('logout/', views.logout,name='logout'),
    # path('pdf/',views.GeneratePdf.as_view()),
]
