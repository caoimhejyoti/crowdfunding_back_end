from django.urls import path
from . import views

urlpatterns = [
    path('festivals/', views.FestivalList.as_view()),
    path('festivals/<int:pk>/', views.FestivalDetail.as_view()),
    # path('festivals/<int:pk>/tickets/', views.TicketList.as_view()),
    path('tickets/', views.TicketList.as_view()),
    ]
