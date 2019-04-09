from django.urls import path
import basketapp.views as basket

app_name = 'basketapp'

urlpatterns = [
    path('', basket.index, name='index'),
    path('add/<int:pk>', basket.add, name='add'),
]
