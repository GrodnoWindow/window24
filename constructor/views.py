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

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'product_type',
                    'placeholder': 'Выберите тип изделия',
                    'label': 'Тип изделия',
                    'data': serializer.data['product_type'],
                },
                {
                    'name': 'profile',
                    'placeholder': 'Выберите Профиль',
                    'label': 'Профиль',
                    'data': serializer.data['profile'],
                },
                {
                    'name': 'aggregate',
                    'placeholder': 'Выберите заполнитель',
                    'label': 'Заполнитель',
                    'data': serializer.data['aggregate'],
                },
                {
                    'name': 'fittings',
                    'placeholder': 'Выберите фурнитуру',
                    'label': 'Фурнитура',
                    'data': serializer.data['fittings'],
                },
                {
                    'name': 'seal_outside',
                    'placeholder': 'Выберите уплотнение снаружи',
                    'label': 'Уплотнение снаружи',
                    'data': serializer.data['seal_outside'],
                },
                {
                    'name': 'seal_rebate',
                    'placeholder': 'Выберите уплотнение притвора',
                    'label': 'Уплотнение притвора',
                    'data': serializer.data['seal_rebate'],
                },
                {
                    'name': 'seal_internal',
                    'placeholder': 'Выберите внутренее уплотнение',
                    'label': 'Уплотнение внутренее',
                    'data': serializer.data['seal_internal'],
                },
                {
                    'name': 'seal_color',
                    'placeholder': 'Выберите цвет уплотнения',
                    'label': 'Цвет уплотнения',
                    'data': serializer.data['seal_color'],
                },
                {
                    'name': 'shpros',
                    'placeholder': 'Выберите шпрос',
                    'label': 'Шпрос',
                    'data': serializer.data['shpros'],
                },
                {
                    'name': 'shtapik',
                    'placeholder': 'Выберите штапик',
                    'label': 'Штапик',
                    'data': serializer.data['shtapik'],
                },
                {
                    'name': 'sash',
                    'placeholder': 'Выберите створку',
                    'label': 'Створка',
                    'data': serializer.data['sash'],
                },
                {
                    'name': 'lamination_outside',
                    'placeholder': 'Выберите наружную ламинацию',
                    'label': 'Ламинация снаружи',
                    'data': serializer.data['lamination_outside'],
                },
                {
                    'name': 'lamination_inside',
                    'placeholder': 'Выберите внутреннюю ламинацию',
                    'label': 'Ламинация внутри',
                    'data': serializer.data['lamination_inside'],
                },
                {
                    'name': 'profile_weight',
                    'placeholder': 'Выберите массу профиля',
                    'label': 'Масса профиля',
                    'data': serializer.data['profile_weight'],

                }

            ]
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
        # filters['windowsill_danke_komfort'] = WindowsillDankeKomfort.objects.all()
        # filters['windowsill_danke_standart'] = WindowsillDankeStandart.objects.all()
        # filters['windowsill_danke_premium'] = WindowsillDankePremium.objects.all()
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

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'products_install',
                    'placeholder': 'Выберите монтаж изделий',
                    'label': 'Монтаж изделий',
                    'data': serializer.data['products_install'],
                },
                {
                    'name': 'pvc_slopes',
                    'placeholder': 'Выберите откосы ПВХ',
                    'label': 'Откосы ПВХ',
                    'data': serializer.data['pvc_slopes'],
                },
                {
                    'name': 'free_positions',
                    'placeholder': 'Выберите бесплатные позиции',
                    'label': 'Бесплатные позиции',
                    'data': serializer.data['free_positions'],
                },

            ]
        })


class ConstructorExtraMaterialAPIView(APIView):

    def get(self, request, *args, **kwargs):
        filters = {}
        #  extramaterial
        filters['windowsill'] = Windowsill.objects.all()
        # filters['windowsill_danke_komfort'] = WindowsillDankeKomfort.objects.all()
        # filters['windowsill_danke_standart'] = WindowsillDankeStandart.objects.all()
        # filters['windowsill_danke_premium'] = WindowsillDankePremium.objects.all()
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

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'windowsill',
                    'placeholder': 'Выберите подоконник',
                    'label': 'Подоконники',
                    'data': serializer.data['windowsill'],
                },
                # {
                #     'name': 'windowsill_danke_komfort',
                #     'placeholder': 'Выберите подоконник Danke Komfort',
                #     'label': 'Подоконники Danke Komfort',
                #     'data': serializer.data['windowsill_danke_komfort'],
                # },
                # {
                #     'name': 'windowsill_danke_standart',
                #     'placeholder': 'Выберите подоконник Danke Standart',
                #     'label': 'Подоконники Danke Standart',
                #     'data': serializer.data['windowsill_danke_standart'],
                # },
                # {
                #     'name': 'windowsill_danke_premium',
                #     'placeholder': 'Выберите подоконник Danke Premium',
                #     'label': 'Подоконники Danke Premium',
                #     'data': serializer.data['windowsill_danke_premium'],
                # },
                {'name': 'low_tides',
                 'placeholder': 'Выберите отливы',
                 'label': 'Отливы',
                 'data': serializer.data['low_tides'], },
                {
                    'name': 'visors',
                    'placeholder': 'Выберите козырьки',
                    'label': 'Козырьки',
                    'data': serializer.data['visors'],
                },
                {
                    'name': 'flashing',
                    'placeholder': 'Выберите нащельники',
                    'label': 'Нащельники',
                    'data': serializer.data['flashing'],
                },
                {
                    'name': 'flashing_metal',
                    'placeholder': 'Выберите металлические нащельники',
                    'label': 'Металлические нащельники',
                    'data': serializer.data['flashing_metal'],
                },
                {
                    'name': 'platband',
                    'placeholder': 'Выберите наличники',
                    'label': 'Наличники',
                    'data': serializer.data['platband'],
                },
                {
                    'name': 'extensions_to_profile60',
                    'placeholder': 'Выберите доборы к профилю 60мм',
                    'label': 'Доборы к профилю 60мм',
                    'data': serializer.data['extensions_to_profile60'],
                },
                {
                    'name': 'extensions_to_profile70',
                    'placeholder': 'Выберите доборы к профилю 70мм',
                    'label': 'Доборы к профилю 70мм',
                    'data': serializer.data['extensions_to_profile70'],
                },
                {
                    'name': 'bay_window_to_profile60',
                    'placeholder': 'Выберите эркер к профилю 60мм',
                    'label': 'Эркер к профилю 60мм',
                    'data': serializer.data['bay_window_to_profile60']

                },
                {
                    'name': 'bay_window_to_profile70',
                    'placeholder': 'Выберите эркер к профилю 70мм',
                    'label': 'Эркер к профилю 70мм',
                    'data': serializer.data['bay_window_to_profile70'],
                },
                {
                    'name': 'connector_90g',
                    'placeholder': 'Выберите соединитель 90гр',
                    'label': 'Соединитель 90гр',
                    'data': serializer.data['connector_90g'],
                },
                {
                    'name': 'accessories',
                    'placeholder': 'Выберите комлпектующие',
                    'label': 'Комлпектующие',
                    'data': serializer.data['accessories'],
                },
                {
                    'name': 'handles',
                    'placeholder': 'Выберите ручку',
                    'label': 'Ручка',
                    'data': serializer.data['handles'],
                },
                {
                    'name': 'locks',
                    'placeholder': 'Выберите замок',
                    'label': 'Замок',
                    'data': serializer.data['locks'],
                },
                {
                    'name': 'straight_connectors',
                    'placeholder': 'Выберите прямые соединители',
                    'label': 'Прямые соединители',
                    'data': serializer.data['straight_connectors'],
                },
                {
                    'name': 'supply_valve',
                    'placeholder': 'Выберите приточный клапан',
                    'label': 'Приточный клапан',
                    'data': serializer.data['supply_valve'],
                }
            ]
        })

#
# class ConstructorViewSet(viewsets.ModelViewSet):
#     queryset = Constructor.objects.all()  # .values().order_by('-id')
#     serializer_class = ConstructorSerializer
#     pagination_class = CustomPagination
