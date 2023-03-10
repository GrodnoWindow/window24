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
        }), required=False, blank=True
    )

    width = ModelChoiceField(
        queryset=WindowsillWidth.objects.all(), empty_label="Выберите полку подоконника", label='Полка подоконник',
        widget=MySelect(attrs={
            'name': 'Полка подоконник',
            'class': 'form-control mb-2',
            'placeholder': 'Полка подоконник',
        }), required=False, blank=True
    )

    windowsill_color = ModelChoiceField(
        queryset=WindowsillColor.objects.all(), empty_label="Выберите цвет подоконника", label='Цвет подоконник',
        widget=MySelect(attrs={
            'name': 'Цвет подоконника',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета подоконник',
        }), required=False, blank=True
    )

    windowsill_plug = ModelChoiceField(
        queryset=WindowsillPlug.objects.all(), empty_label="Выберите заглушку", label='Заглушка',
        widget=MySelect(attrs={
            'name': 'Заглушка',
            'class': 'form-control mb-2',
            'placeholder': 'Заглушка',
        }), required=False, blank=True
    )

    windowsill_connection = ModelChoiceField(
        queryset=WindowsillConnection.objects.all(), empty_label="Выберите соединитель", label='Соединитель',
        widget=MySelect(attrs={
            'name': 'Соединитель',
            'class': 'form-control mb-2',
            'placeholder': 'Соединитель',
        }), required=False, blank=True
    )

    class Meta:
        model = WindowsillCalc
        fields = ['windowsill', 'windowsill_color', 'width', 'length','windowsill_plug','windowsill_plug_count','windowsill_connection','windowsill_connection_count',  'count']
        widgets = {
            'windowsill_plug_count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество заглушек'
            }),
            'windowsill_connection_count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество соединителей'
            }),
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


class VisorsCalcForm(ModelForm):
    visors = ModelChoiceField(
        queryset=Visors.objects.all(), empty_label="Выберите козырек", label='Козырек',
        widget=MySelect(attrs={
            'name': 'Козырек',
            'class': 'form-control mb-2',
            'placeholder': 'Козырек',
        })
    )

    class Meta:
        model = VisorsCalc
        fields = ['visors', 'width', 'length', 'count']
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


class FlashingCalcForm(ModelForm):
    flashing = ModelChoiceField(
        queryset=Flashing.objects.all(), empty_label="Выберите нащельник", label='Нащельник',
        widget=MySelect(attrs={
            'name': 'Нащельник',
            'class': 'form-control mb-2',
            'placeholder': 'Нащельник',
        })
    )

    class Meta:
        model = VisorsCalc
        fields = ['flashing', 'width', 'length', 'count']
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


class CasingCalcForm(ModelForm):
    casing = ModelChoiceField(
        queryset=Casing.objects.all(), empty_label="Выберите наличник", label='Наличники',
        widget=MySelect(attrs={
            'name': 'Наличники',
            'class': 'form-control mb-2',
            'placeholder': 'Наличники',
        })
    )

    class Meta:
        model = CasingCalc
        fields = ['casing', 'width', 'length', 'count']
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


class SlopesOfMetalCalcForm(ModelForm):
    slopes_of_metal = ModelChoiceField(
        queryset=SlopesOfMetal.objects.all(), empty_label="Выберите откос из металла", label='Откос из металла',
        widget=MySelect(attrs={
            'name': 'Откос из металла',
            'class': 'form-control mb-2',
            'placeholder': 'Откос из металла',
        })
    )

    class Meta:
        model = SlopesOfMetalCalc
        fields = ['slopes_of_metal', 'width', 'length', 'count']
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


class InternalSlopesCalcForm(ModelForm):
    internal_slopes = ModelChoiceField(
        queryset=InternalSlopes.objects.all(), empty_label="Выберите откосы", label='Откосы',
        widget=MySelect(attrs={
            'name': 'Откосы',
            'class': 'form-control mb-2',
            'placeholder': 'откосы',
        })
    )

    class Meta:
        model = InternalSlopesCalc
        fields = ['internal_slopes', 'width', 'length', 'count']
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


class MountingMaterialsCalcForm(ModelForm):
    mounting_materials = ModelChoiceField(
        queryset=MountingMaterials.objects.all(), empty_label="Выберите монтажные материалы",
        label='Монтажные материалы',
        widget=MySelect(attrs={
            'name': 'Монтажые материалы',
            'class': 'form-control mb-2',
            'placeholder': 'Монтажные материалы',
        })
    )

    class Meta:
        model = MountingMaterialsCalc
        fields = ['mounting_materials', 'count']
        widgets = {
            'count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class WorksCalcForm(ModelForm):
    works = ModelChoiceField(
        queryset=Works.objects.all(), empty_label="Выберите работу",
        label='Работы',
        widget=MySelect(attrs={
            'name': 'Работы',
            'class': 'form-control mb-2',
            'placeholder': 'Работы',
        })
    )

    class Meta:
        model = WorksCalc
        fields = ['works', 'count']
        widgets = {
            'count': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }
