from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question")  # Removed 'language' since it's not a field anymore
    search_fields = ("question",)  # Allows searching by question

admin.site.register(FAQ, FAQAdmin)
