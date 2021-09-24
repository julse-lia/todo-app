from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # path('add_todo/', views.add_todo_item, name="add_item"),
    path('add_todo/', views.CreateView.as_view(), name="add_item"),
    path('detail/<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('delete_item/<int:pk>/', views.DeleteView.as_view(), name="delete_item"),
    path('update_item/<int:pk>/', views.UpdateView.as_view(), name="update_item")
]

