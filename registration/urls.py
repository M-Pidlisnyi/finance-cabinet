from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    path('profile/edit/<int:pk>', lambda req, pk: HttpResponseNotFound(content="not implemented"), name='profile-edit' ),
]