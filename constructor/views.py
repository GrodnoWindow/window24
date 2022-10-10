from .models import Constructor
from .serializer import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from config.pagination import CustomPagination
from rest_framework import views
from call.models import Call
from client.models import Client
from .models import *


class ConstructorWindowAPIView(APIView):

    def get(self, request, *args, **kwargs):
        filters = {}
        filters['product_type'] = ProductType.objects.all()
        filters['profile'] = Profile.objects.all()
        filters['aggregate'] = Aggregate.objects.all()
        filters['fittings'] = Fittings.objects.all()
        filters['seal_outside'] = SealOutside.objects.all()
        filters['seal_rebate'] = SealRebate.objects.all()
        filters['seal_internal'] = SealInternal.objects.all()
        filters['seal_color'] = SealColor.objects.all()
        filters['shpros'] = Shpros.objects.all()
        filters['shtapik'] = Shtapik.objects.all()
        filters['sash'] = Sash.objects.all()
        filters['lamination_outside'] = LaminationOutside.objects.all()
        filters['lamination_inside'] = LaminationInside.objects.all()
        filters['profile_weight'] = ProfileWeight.objects.all()

        serializer = ConstructorFieldsSerializer(filters)
        return Response({
            'product_type': [
                {'placeholder': 'Тип изделия',
                 'label': 'Выберите тип изделия',
                 'data': serializer.data['product_type'], }
            ],
            'profile': [
                {'placeholder': 'Профиль',
                 'label': 'Выберите профиль',
                 'data': serializer.data['profile'], }
            ],
            'aggregate': [
                {'placeholder': 'Заполнитель',
                 'label': 'Выберите заполнитель',
                 'data': serializer.data['aggregate'], }
            ],
            'fittings': [
                {'placeholder': 'Фурнитура',
                 'label': 'Выберите фурнитуру',
                 'data': serializer.data['fittings'], }
            ],
            'seal_outside': [
                {'placeholder': 'Уплотнение снаружи',
                 'label': 'Выберите уплотнение снаружи',
                 'data': serializer.data['seal_outside'], }
            ],
            'seal_rebate': [
                {'placeholder': 'Уплотнение притвора',
                 'label': 'Выберите уплотнение притвора',
                 'data': serializer.data['seal_rebate'], }
            ],
            'seal_internal': [
                {'placeholder': 'Уплотнение внутренее',
                 'label': 'Выберите внутренее уплотнение',
                 'data': serializer.data['seal_internal'], }
            ],
            'seal_color': [
                {'placeholder': 'Цвет уплотнения',
                 'label': 'Выберите цвет уплотнения',
                 'data': serializer.data['seal_color'], }
            ],
            'shpros': [
                {'placeholder': 'Шпрос',
                 'label': 'Выберите шпрос',
                 'data': serializer.data['shpros'], }
            ],
            'shtapik': [
                {'placeholder': 'Штапик',
                 'label': 'Выберите штапик',
                 'data': serializer.data['shtapik'], }
            ],
            'sash': [
                {'placeholder': 'Створка',
                 'label': 'Выберите створку',
                 'data': serializer.data['sash'], }
            ],
            'lamination_outside': [
                {'placeholder': 'Ламинация снаружи',
                 'label': 'Выберите наружную ламинацию',
                 'data': serializer.data['lamination_outside'], }
            ],
            'lamination_inside': [
                {'placeholder': 'Ламинация внутри',
                 'label': 'Выберите внутреннюю ламинацию',
                 'data': serializer.data['lamination_inside'], }
            ],
            'profile_weight': [
                {'placeholder': 'Масса профиля',
                 'label': 'Выберите массу профиля',
                 'data': serializer.data['profile_weight'], }
            ],

        })


class ConstructorExtraWorkAPIView(APIView):

    def get(self, request, *args, **kwargs):
        filters = {}
        # other
        filters['products_install'] = ProductsInstall.objects.all()
        filters['pvc_slopes'] = PvcSlopes.objects.all()
        filters['free_positions'] = FreePositions.objects.all()
        filters['favorite_positions'] = FavoritePositions.objects.all()
        #
        filters['windowsill'] = Windowsill.objects.all()
        filters['windowsill_danke_komfort'] = WindowsillDankeKomfort.objects.all()
        filters['windowsill_danke_standart'] = WindowsillDankeStandart.objects.all()
        filters['windowsill_danke_premium'] = WindowsillDankePremium.objects.all()
        filters['low_tides'] = LowTides.objects.all()
        filters['visors'] = Visors.objects.all()
        filters['flashing'] = Flashing.objects.all()
        filters['flashing_metal'] = FlashingMetal.objects.all()
        filters['platband'] = Platband.objects.all()
        filters['extensions_to_profile60'] = ExtensionsToProfile60.objects.all()
        filters['extensions_to_profile70'] = ExtensionsToProfile70.objects.all()
        filters['bay_window_to_profile60'] = BayWindowToProfile60.objects.all()
        filters['bay_window_to_profile70'] = BayWindowToProfile70.objects.all()
        filters['connector_90g'] = Connector90g.objects.all()
        filters['accessories'] = Accessories.objects.all()
        filters['handles'] = Handles.objects.all()
        filters['locks'] = Locks.objects.all()
        filters['straight_connectors'] = StraightConnectors.objects.all()
        filters['supply_valve'] = SupplyValve.objects.all()

        serializer = ConstructorFieldsSerializer(filters)
        return Response({
            'products_install': [
                {'placeholder': 'Монтаж изделий',
                 'label': 'Выберите монтаж изделий',
                 'data': serializer.data['products_install'], }
            ],
            'pvc_slopes': [
                {'placeholder': 'Откосы ПВХ',
                 'label': 'Выберите откосы ПВХ',
                 'data': serializer.data['pvc_slopes'], }
            ],
            'free_positions': [
                {'placeholder': 'Бесплатные позиции',
                 'label': 'Выберите бесплатные позиции',
                 'data': serializer.data['free_positions'], }
            ],
        })


class ConstructorExtraMaterialAPIView(APIView):

    def get(self, request, *args, **kwargs):
        filters = {}
        #  extramaterial
        filters['windowsill'] = Windowsill.objects.all()
        filters['windowsill_danke_komfort'] = WindowsillDankeKomfort.objects.all()
        filters['windowsill_danke_standart'] = WindowsillDankeStandart.objects.all()
        filters['windowsill_danke_premium'] = WindowsillDankePremium.objects.all()
        filters['low_tides'] = LowTides.objects.all()
        filters['visors'] = Visors.objects.all()
        filters['flashing'] = Flashing.objects.all()
        filters['flashing_metal'] = FlashingMetal.objects.all()
        filters['platband'] = Platband.objects.all()
        filters['extensions_to_profile60'] = ExtensionsToProfile60.objects.all()
        filters['extensions_to_profile70'] = ExtensionsToProfile70.objects.all()
        filters['bay_window_to_profile60'] = BayWindowToProfile60.objects.all()
        filters['bay_window_to_profile70'] = BayWindowToProfile70.objects.all()
        filters['connector_90g'] = Connector90g.objects.all()
        filters['accessories'] = Accessories.objects.all()
        filters['handles'] = Handles.objects.all()
        filters['locks'] = Locks.objects.all()
        filters['straight_connectors'] = StraightConnectors.objects.all()
        filters['supply_valve'] = SupplyValve.objects.all()

        serializer = ConstructorFieldsSerializer(filters)
        return Response({
            'windowsill': [
                {'placeholder': 'Подоконники',
                 'label': 'Выберите подоконник',
                 'data': serializer.data['windowsill'], }
            ],
            'windowsill_danke_komfort': [
                {'placeholder': 'Подоконники Danke Komfort',
                 'label': 'Выберите подоконник Danke Komfort',
                 'data': serializer.data['windowsill_danke_komfort'], }
            ],
            'windowsill_danke_standart': [
                {'placeholder': 'Подоконники Danke Standart',
                 'label': 'Выберите подоконник Danke Standart',
                 'data': serializer.data['windowsill_danke_standart'], }
            ],
            'windowsill_danke_premium': [
                {'placeholder': 'Подоконники Danke Premium',
                 'label': 'Выберите подоконник Danke Premium',
                 'data': serializer.data['windowsill_danke_premium'], }
            ],
            'low_tides': [
                {'placeholder': 'Отливы',
                 'label': 'Выберите отливы',
                 'data': serializer.data['low_tides'], }
            ],
            'visors': [
                {'placeholder': 'Козырьки',
                 'label': 'Выберите козырьки',
                 'data': serializer.data['visors'], }
            ],
            'flashing': [
                {'placeholder': 'Нащельники',
                 'label': 'Выберите нащельники',
                 'data': serializer.data['flashing'], }
            ],
            'flashing_metal': [
                {'placeholder': 'Металлические нащельники',
                 'label': 'Выберите металлические нащельники',
                 'data': serializer.data['flashing_metal'], }
            ],
            'platband': [
                {'placeholder': 'Наличники',
                 'label': 'Выберите наличники',
                 'data': serializer.data['platband'], }
            ],
            'extensions_to_profile60': [
                {'placeholder': 'Доборы к профилю 60мм',
                 'label': 'Выберите доборы к профилю 60мм',
                 'data': serializer.data['extensions_to_profile60'], }
            ],
            'extensions_to_profile70': [
                {'placeholder': 'Доборы к профилю 70мм',
                 'label': 'Выберите доборы к профилю 70мм',
                 'data': serializer.data['extensions_to_profile70'], }
            ],
            'bay_window_to_profile60': [
                {'placeholder': 'Эркер к профилю 60мм',
                 'label': 'Выберите эркер к профилю 60мм',
                 'data': serializer.data['bay_window_to_profile60'], }
            ],
            'bay_window_to_profile70': [
                {'placeholder': 'Эркер к профилю 70мм',
                 'label': 'Выберите эркер к профилю 70мм',
                 'data': serializer.data['bay_window_to_profile70'], }
            ],
            'connector_90g': [
                {'placeholder': 'Соединитель 90гр',
                 'label': 'Выберите соединитель 90гр',
                 'data': serializer.data['connector_90g'], }
            ],
            'accessories': [
                {'placeholder': 'Комлпектующие',
                 'label': 'Выберите комлпектующие',
                 'data': serializer.data['accessories'], }
            ],
            'handles': [
                {'placeholder': 'Ручка',
                 'label': 'Выберите ручку',
                 'data': serializer.data['handles'], }
            ],
            'locks': [
                {'placeholder': 'Замок',
                 'label': 'Выберите замок',
                 'data': serializer.data['locks'], }
            ],
            'straight_connectors': [
                {'placeholder': 'Прямые соединители',
                 'label': 'Выберите прямые соединители',
                 'data': serializer.data['straight_connectors'], }
            ],
            'supply_valve': [
                {'placeholder': 'Приточный клапан',
                 'label': 'Выберите приточный клапан',
                 'data': serializer.data['supply_valve'], }
            ],

        })


class ConstructorViewSet(viewsets.ModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    pagination_class = CustomPagination
