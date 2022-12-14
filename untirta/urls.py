"""untirta URL Configuration

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
from feb.views import prodi1
from fh.views import prodi2
from fisip.views import prodi3
from fk.views import prodi4
from fkip.views import prodi5
from fp.views import prodi6
from ft.views import prodi7
from pascasarjana.views import prodi8
from profil.views import profil
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feb/', prodi1),
    path('fh/', prodi2),
    path('fisip/', prodi3),
    path('fk/', prodi4),
    path('fkip/', prodi5),
    path('fp/', prodi6),
    path('ft/', prodi7),
    path('pascasarjana/', prodi8),
    path('profil/', profil),
    path('', views.index),
    
]
