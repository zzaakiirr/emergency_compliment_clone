from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/new_compliment', views.get_new_compliment, name="get_new_compliment"),
]
