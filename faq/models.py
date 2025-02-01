# faq/models.py

from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    translated_answer = models.TextField(null=True, blank=True)  # Add this if missing

    def translate(self):
        """Automatically translate question and answer into various languages"""
        translator = Translator()

        # Translate question and answer into multiple languages
        languages = ["hi", "bn", "es", "fr", "de", "it", "pt"]  # You can add more languages as needed
        for lang in languages:
            if lang not in self.translations:
                self.translations[lang] = {
                    "question": translator.translate(self.question, src="en", dest=lang).text,
                    "answer": translator.translate(self.answer, src="en", dest=lang).text
                }
        self.save()

    def get_translated_faq(self, lang):
        """Retrieve the translated version of FAQ based on lang parameter"""
        # If the translation exists for the specified language, return it; otherwise, return English (default)
        return self.translations.get(lang, {"question": self.question, "answer": self.answer})
