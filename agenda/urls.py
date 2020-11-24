"""agenda URL Configuration

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
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.evento_submit),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('agenda/lista/', views.json_lista_evento),
    path('', views.index),
    path('login/', views.login_user),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
