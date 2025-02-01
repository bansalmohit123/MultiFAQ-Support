from django.urls import path
from .views import FAQListView,FAQCreateView

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
     path("faqs/create/", FAQCreateView.as_view(), name="faq-create"),
]
