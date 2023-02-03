from django.urls import path
from . import views


urlpatterns = [
    path('propriedades/', views.PropriedadeView().as_view()),
]