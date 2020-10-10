from django.urls import path

from . import views
from .views import HelloQueryView

urlpatterns = [
    path('', HelloQueryView.as_view()),
]

