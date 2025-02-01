# from rest_framework import serializers
# from .models import FAQ
# from googletrans import Translator

# translator = Translator()

# class FAQSerializer(serializers.ModelSerializer):
#     translated_question = serializers.SerializerMethodField()
#     translated_answer = serializers.SerializerMethodField()

#     def get_translated_question(self, obj):
#         lang = self.context.get("request").query_params.get("lang", "en")
#         try:
#             return translator.translate(obj.question, dest=lang).text
#         except Exception as e:
#             return obj.question  # Fallback to original text if translation fails

#     def get_translated_answer(self, obj):
#         lang = self.context.get("request").query_params.get("lang", "en")
#         try:
#             return translator.translate(obj.answer, dest=lang).text
#         except Exception as e:
#             return obj.answer  # Fallback to original text if translation fails

#     class Meta:
#         model = FAQ
#         fields = ["id", "question", "translated_question", "answer", "translated_answer"]  # Added translated_answer
from rest_framework import serializers
from django.core.cache import cache
from .models import FAQ
from googletrans import Translator

translator = Translator()

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()
    translated_answer = serializers.SerializerMethodField()

    def get_translated_text(self, text, lang, field_name, obj_id):
        """Retrieve translation from cache or translate & cache it."""
        cache_key = f"faq_{obj_id}_{field_name}_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation  # Return cached translation if available

        try:
            translated_text = translator.translate(text, dest=lang).text
            cache.set(cache_key, translated_text, timeout=86400)  # Cache for 24 hours
            return translated_text
        except Exception as e:
            return text  # Fallback to original text if translation fails

    def get_translated_question(self, obj):
        lang = self.context.get("request").query_params.get("lang", "en")
        return self.get_translated_text(obj.question, lang, "question", obj.id)

    def get_translated_answer(self, obj):
        lang = self.context.get("request").query_params.get("lang", "en")
        return self.get_translated_text(obj.answer, lang, "answer", obj.id)

    class Meta:
        model = FAQ
        fields = ["id", "question", "translated_question", "answer", "translated_answer"]
