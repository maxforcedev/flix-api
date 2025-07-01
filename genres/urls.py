from django.urls import path
from . import views


urlpatterns = [

    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-crud'),
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),

]
