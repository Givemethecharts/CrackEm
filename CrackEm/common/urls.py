from django.urls import path

from CrackEm.common import views

urlpatterns = (path('', views.home_page, name='home-page'),)