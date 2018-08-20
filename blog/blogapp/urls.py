from django.urls import path
from . import views

app_name = 'blogapp' # for namespacing
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_blogpost/', views.add_blogpost, name='add_blogpost'),
    path('delete_blogpost/', views.delete_blogpost, name='delete_blogpost'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
]
