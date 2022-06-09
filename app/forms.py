from django import forms
from datetime import date
from .models import Product


class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    last_narne = forms.CharField(label="Фамилия автора")
    date_of_Ьirth = forms.DateField(label="Дaтa рождения",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label="Дaтa смерти",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
