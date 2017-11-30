"""Becas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, login_required
from apps import views
from users.views import RegisterUsers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^basetec/',login_required(views.base),name='base_view'),
    url(r'^$', login, {'template_name': 'apps/Index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name="logout"),
    url(r'^registro/',views.Registro_view,name='Registrar_view'),
    url(r'^chequeo/', views.Chequeo_view,name="Chequeo_view"),
    url(r'^register/', RegisterUsers.as_view(), name="registrar"),
    url(r'^historial/',views.Becarios_report.as_view(),name="historial")
]
