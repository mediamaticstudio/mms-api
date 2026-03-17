from django.urls import path
from .views import ContactMailView, GetQuoteMailView, MarketingAuditView, PodcastBookingView

urlpatterns = [
    path("send/", ContactMailView.as_view(), name="contact-mail"),
    path("quote/", GetQuoteMailView.as_view(), name="get-quote"),
    path("marketing-audit/", MarketingAuditView.as_view(), name="marketing-audit"),
    path("podcast-booking/", PodcastBookingView.as_view(), name="podcast-booking"),
]
