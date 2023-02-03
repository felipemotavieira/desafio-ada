from django.urls import path
from . import views


urlpatterns = [
    path('contas/', views.ContaView().as_view()),
]
