from django.contrib.admin.widgets import AdminDateWidget

from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, ChoiceField, ModelChoiceField, DateField, NumberInput
from django import forms


class MySelect(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        return u'<option whatever>...</option>'


class OrderForm(ModelForm):
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
        fields = ['address', 'name', 'phone', 'date', 'status']
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


class WindowsillCalcForm(ModelForm):
    windowsill = ModelChoiceField(
        queryset=Windowsill.objects.filter(unit=1), empty_label="Выберите подоконник", label='Подоконник',
        widget=MySelect(attrs={
            'name': 'Подоконник',
            'class': 'form-control mb-2',
            'placeholder': 'Подоконник',
        })
    )

    width = ModelChoiceField(
        queryset=WindowsillWidth.objects.all(), empty_label="Выберите полку подоконника", label='Полка подоконник',
        widget=MySelect(attrs={
            'name': 'Полка подоконник',
            'class': 'form-control mb-2',
            'placeholder': 'Полка подоконник',
        })
    )

    class Meta:
        model = WindowsillCalc
        fields = ['windowsill', 'width', 'length', 'count']
        widgets = {
            'length': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class WindowsillComplectCalcForm(ModelForm):
    windowsill = ModelChoiceField(
        queryset=Windowsill.objects.filter(unit=2), empty_label="Выберите комплектующие", label='Комплектующие',
        widget=MySelect(attrs={
            'name': 'Комплектующие',
            'class': 'form-control mb-2',
            'placeholder': 'Подоконник',
        })
    )

    class Meta:
        model = WindowsillComplectCalc
        fields = ['windowsill', 'count']
        widgets = {
            'count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class LowTidesCalcForm(ModelForm):
    low_tides = ModelChoiceField(
        queryset=LowTides.objects.filter(unit=1), empty_label="Выберите отлив", label='Отливы',
        widget=MySelect(attrs={
            'name': 'Отлив',
            'class': 'form-control mb-2',
            'placeholder': 'Отлив',
        })
    )

    class Meta:
        model = LowTidesCalc
        fields = ['low_tides', 'width', 'length', 'count']
        widgets = {
            'length': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'width': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина'
            }),
            'count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class LowTidesComplectCalcForm(ModelForm):
    low_tides = ModelChoiceField(
        queryset=LowTides.objects.filter(unit=2), empty_label="Выберите комплектующие", label='Комплектующие',
        widget=MySelect(attrs={
            'name': 'Комплектующие',
            'class': 'form-control mb-2',
            'placeholder': 'Подоконник',
        })
    )

    class Meta:
        model = LowTidesComplectCalc
        fields = ['low_tides', 'count']
        widgets = {
            'count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }
