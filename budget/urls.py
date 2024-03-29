from django.urls import path

from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit_expanse', views.edit_expanse, name='edit_expanse'),
    path('<int:pk>/remove_expanse', views.remove_expanse, name='remove_expanse'),
    path('<int:pk>/expanse/', views.expanse, name='expanse'),
    path('<int:pk>/status/', views.status, name='status'),
]