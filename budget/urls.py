from django.urls import path

from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/expanse/', views.expanse, name='expanse'),
    path('<int:pk>/status/', views.status, name='status'),
]