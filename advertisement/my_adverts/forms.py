from django import forms
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'category', 'auction', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control-lg'}),
            'category': forms.NumberInput(attrs={'class': 'form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': forms.FileInput(),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака!")
        return title







