from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/<int:pk>/', views.FinAccountDetailView.as_view(), name='account-detail'),
    path('account/open/', views.open_account, name='finacc-open'),
    path('account/close/<int:pk>', views.close_account, name='finacc-close'),
]