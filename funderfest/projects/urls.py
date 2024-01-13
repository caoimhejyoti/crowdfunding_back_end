from django.urls import path
from . import views

urlpatterns = [
    path('festivals/', views.FestivalList.as_view()),
    path('festivals/<int:pk>/', views.FestivalDetail.as_view()),
    ]
