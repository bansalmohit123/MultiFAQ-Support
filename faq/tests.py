from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", language="en")

    def test_faq_creation(self):
        faq = FAQ.objects.get(question="What is Django?")
        self.assertEqual(faq.answer, "Django is a web framework.")
