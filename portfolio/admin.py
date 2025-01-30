from django.contrib import admin
from .models import JobOffer

# Регистрируем модель JobOffer в админке
admin.site.register(JobOffer)
