from django.urls import path

from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:entry_id>/expanse/', views.expanse, name='expanse'),
]