from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='batch-home'),
    path('batchInRequest', views.batchInRequest),
    path('batchOutRequest', views.batchOutRequest)
]
