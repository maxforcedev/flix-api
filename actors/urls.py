from django.urls import path
from . import views


urlpatterns = [

    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-crud'),
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),

]