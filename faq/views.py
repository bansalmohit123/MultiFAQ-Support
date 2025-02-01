# from rest_framework.generics import ListAPIView
# from .models import FAQ
# from .serializers import FAQSerializer

# class FAQListView(ListAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer

#     def get_serializer_context(self):
#         return {"request": self.request}
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from googletrans import Translator
from .models import FAQ
from .serializers import FAQSerializer

translator = Translator()

class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        return {"request": self.request}

class FAQCreateView(APIView):
    """API endpoint to store FAQs in the database."""
    
    def post(self, request):
        question = request.data.get("question")
        answer = request.data.get("answer")

        if not question or not answer:
            return Response({"error": "Both question and answer are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Save FAQ to the database
        faq = FAQ.objects.create(question=question, answer=answer)

        # Store translations in Redis cache for faster access
        languages = ["hi", "bn", "fr", "es"]  # Hindi, Bengali, French, Spanish
        for lang in languages:
            translated_q = translator.translate(question, dest=lang).text
            translated_a = translator.translate(answer, dest=lang).text

            cache.set(f"faq_{faq.id}_question_{lang}", translated_q, timeout=86400)  # Cache for 1 day
            cache.set(f"faq_{faq.id}_answer_{lang}", translated_a, timeout=86400)

        return Response({"message": "FAQ created successfully!", "id": faq.id}, status=status.HTTP_201_CREATED)
