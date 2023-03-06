from django.contrib.admin.widgets import AdminDateWidget

from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, ChoiceField, ModelChoiceField, DateField, NumberInput
from django import forms


class MySelect(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        return u'<option whatever>...</option>'


class OrderForm(ModelForm):
    # status = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS)
    # icons = forms.ModelChoiceField(
    #     queryset=Windowsill.objects.filter(unit=2),
    #     widget=MySelect(attrs={'id': 'sum_in_byn'})
    # )

    status = ModelChoiceField(
        queryset=Status.objects.all(), empty_label="Выберите статус", label='Статус',
        widget=MySelect(attrs={
            'name': 'Статус',
            'class': 'form-control mb-2',
            'placeholder': 'Статус замера',
        })
    )
    # date = DateField(widget=AdminDateWidget)
    date = forms.DateTimeField(label="Дата замера", required=True, widget=NumberInput(
        attrs={
            'type': 'date',
            'class': 'form-control mb-2',
        }))

    class Meta:
        model = Order
        fields = ['address', 'name', 'phone', 'date','status']
        widgets = {
            'address': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Адрес замера'
            }),

            'name': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Имя заказчика'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Номер телефона'
            }),

        }
