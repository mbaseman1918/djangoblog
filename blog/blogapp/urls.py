from django.urls import path
from . import views

app_name = 'blogapp' # for namespacing
urlpatterns = [
    path('index/', views.index, name='index'),
]
