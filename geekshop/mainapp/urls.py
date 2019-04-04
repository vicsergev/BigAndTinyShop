from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),

    path('catalog/', mainapp.catalog, name='catalog'),

    path('<int:pk>', mainapp.category, name='category'),

    path('contacts/', mainapp.contacts, name='contacts'),
]
