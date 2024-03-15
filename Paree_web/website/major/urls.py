from django.urls import path
from major import views

urlpatterns = [
     path('', views.index, name='index'),
     path('predict', views.predict, name='predict'),
]