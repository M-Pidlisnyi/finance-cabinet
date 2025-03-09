from django.urls import path
from django.views.generic import TemplateView
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
]