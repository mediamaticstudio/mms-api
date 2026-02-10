from django.urls import path
from .views import ContactMailView

urlpatterns = [
    path("send/", ContactMailView.as_view(), name="contact-mail"),
]
