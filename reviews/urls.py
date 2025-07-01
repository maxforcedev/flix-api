from django.urls import path
from . import views


urlpatterns = [
   
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='reviews-crud'),
    path('reviews/', views.ReviewCreateListView.as_view(), name='reviews-create-list'),

]
