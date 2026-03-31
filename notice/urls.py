from django.urls import path
from . import views

urlpatterns = [

path('add/', views.add_notice, name="add_notice"),
path('view/', views.view_notice, name="view_notice"),
path('delete/<int:id>/', views.delete_notice),

]