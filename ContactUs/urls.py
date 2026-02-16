from django.urls import path
from .views import ContactMailView, GetQuoteMailView

urlpatterns = [
    path("send/", ContactMailView.as_view(), name="contact-mail"),
    path("quote/", GetQuoteMailView.as_view(), name="get-quote"),
]
