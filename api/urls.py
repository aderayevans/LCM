from django.urls import path, include

from . import views

urlpatterns = [
    path('champions', views.ListCreateChampionView.as_view(), name='champions'),
    path('champions/<int:pk>', views.UpdateDeleteChampionView.as_view(), name='champion-detail'),
]