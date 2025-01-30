from django import forms
from .models import JobOffer

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control custom-input',  # добавляем класс для стилизации
                'style': 'font-size: 18px; padding: 10px;',  # добавляем стиль
                'placeholder': 'Введите название компании'  # добавляем плейсхолдер
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control custom-input',  # добавляем класс для стилизации
                'style': 'font-size: 18px; padding: 10px;',  # добавляем стиль
                'placeholder': 'Введите ваш Email'  # добавляем плейсхолдер
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control custom-input',  # добавляем класс для стилизации
                'style': 'font-size: 18px; padding: 10px;',  # добавляем стиль
                'rows': 4,  # количество строк
                'placeholder': 'Опишите вакансию'  # добавляем плейсхолдер
            }),
        }
