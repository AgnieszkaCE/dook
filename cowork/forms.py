from django import forms
from cowork.models import *


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )
        labels = {
            'name': 'Company name'
        }


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'total_desks', 'reserved_desks', 'price')


class DeskCreateForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ('rent_start_date', 'rent_end_date')
