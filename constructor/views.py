from rest_framework.generics import get_object_or_404

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
from calculation.models import Constructor


class EquipmentMainAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['product_type'] = ProductType.objects.all()
        filters['profile'] = Profile.objects.all()
        filters['aggregate'] = Aggregate.objects.all()
        filters['fittings'] = Fittings.objects.all()

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

            ]
        })


class EquipmentExtraAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['shtapik'] = Shtapik.objects.all()
        filters['sash'] = Sash.objects.all()
        filters['gorbylki'] = Gorbylki.objects.all()
        filters['handles'] = Handles.objects.all()
        filters['other_complectation'] = OtherComplectation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
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
                    'name': 'gorbylki',
                    'placeholder': 'Выберите горбыльки',
                    'label': 'Горбыльки',
                    'data': serializer.data['gorbylki'],
                },
                {
                    'name': 'handles',
                    'placeholder': 'Выберите ручки',
                    'label': 'Ручка',
                    'data': serializer.data['handles'],
                },
                {
                    'name': 'other_complectation',
                    'placeholder': 'Выберите доп. комплектацию',
                    'label': 'Дополнительная комплектая',
                    'data': serializer.data['other_complectation'],
                }

            ]
        })


class LaminationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['type_lamination'] = TypeLamination.objects.all()
        filters['type_lamination1'] = TypeLamination2.objects.all()
        filters['seal_internal'] = SealInternal.objects.all()
        filters['seal_outside'] = SealOutside.objects.all()
        filters['seal_basic'] = SealBasic.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'type_lamination',
                    'placeholder': 'Выберите тип ламинации',
                    'label': 'Тип ламинации',
                    'data': serializer.data['type_lamination'],
                },
                {
                    'name': 'type_lamination1',
                    'placeholder': 'Выберите вид ламинации',
                    'label': 'Вид ламинации',
                    'data': serializer.data['type_lamination1'],
                },
                {
                    'name': 'seal_internal',
                    'placeholder': 'Выберите исполнение внутри',
                    'label': 'Исполнение внутри',
                    'data': serializer.data['seal_internal'],
                },
                {
                    'name': 'seal_outside',
                    'placeholder': 'Выберите исполнение снаружи',
                    'label': 'Исполнение снаружи',
                    'data': serializer.data['seal_outside'],
                },
                {
                    'name': 'seal_basic',
                    'placeholder': 'Выберите исполнение основы детали',
                    'label': 'Исполнение основы детали',
                    'data': serializer.data['seal_basic'],
                },

            ]
        })


class DoorAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['product_type'] = ProductTypeDoor.objects.all()
        filters['opening'] = Opening.objects.all()
        filters['lock'] = Lock.objects.all()
        filters['handle'] = DoorHandles.objects.all()
        filters['door_hinges'] = DoorHinges.objects.all()
        filters['cylinder'] = Cylinder.objects.all()
        filters['door_closer'] = DoorCloser.objects.all()
        filters['opening_limiter'] = OpeningLimiter.objects.all()

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
                    'name': 'opening',
                    'placeholder': 'Выберите открывание',
                    'label': 'Открывание',
                    'data': serializer.data['opening'],
                },
                {
                    'name': 'lock',
                    'placeholder': 'Выберите замок',
                    'label': 'Замок',
                    'data': serializer.data['lock'],
                },
                {
                    'name': 'handle',
                    'placeholder': 'Выберите дверные ручки',
                    'label': 'Дверные ручки',
                    'data': serializer.data['handle'],
                },
                {
                    'name': 'door_hinges',
                    'placeholder': 'Выберите дверные петли',
                    'label': 'Дверные петли',
                    'data': serializer.data['door_hinges'],
                },
                {
                    'name': 'cylinder',
                    'placeholder': 'Выберите цилиндр',
                    'label': 'Цилиндр',
                    'data': serializer.data['cylinder'],
                },
                {
                    'name': 'door_closer',
                    'placeholder': 'Выберите доводчик',
                    'label': 'Доводчик',
                    'data': serializer.data['door_closer'],
                },
                {
                    'name': 'opening_limiter',
                    'placeholder': 'Выберите ограничитель открывания',
                    'label': 'Ограничитель открывания',
                    'data': serializer.data['opening_limiter'],
                },

            ]
        })


class ConnectionProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['profile'] = Profile.objects.all()
        filters['article'] = Article.objects.all()
        filters['connection_profile_name'] = ConnectionProfileName.objects.all()
        filters['color_inside'] = ColorInside.objects.all()
        filters['color_outside'] = ColorOutside.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'profile',
                    'placeholder': 'Выберите профиль',
                    'label': 'Профиль',
                    'data': serializer.data['profile'],
                },
                {
                    'name': 'article',
                    'placeholder': 'Выберите артикуль',
                    'label': 'Артикуль',
                    'data': serializer.data['article'],
                },
                {
                    'name': 'connection_profile_name',
                    'placeholder': 'Выберите название',
                    'label': 'Название',
                    'data': serializer.data['connection_profile_name'],
                },
                {
                    'name': 'color_inside',
                    'placeholder': 'Выберите цвет внутри',
                    'label': 'Цвет внутри',
                    'data': serializer.data['color_inside'],
                },
                {
                    'name': 'color_outside',
                    'placeholder': 'Выберите цвет снаружи',
                    'label': 'Цвет снаружи',
                    'data': serializer.data['color_outside'],
                },
            ]
        })


class AdditionalProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['article'] = ArticleAdditionalProfile.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'article',
                    'placeholder': 'Выберите Артикул',
                    'label': 'Артикул',
                    'data': serializer.data['article'],
                },
            ]
        })


class SealantAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['sealant_color'] = SealantColor.objects.all()
        filters['sealant_inside'] = SealantInside.objects.all()
        filters['sealant_outside'] = SealantOutside.objects.all()
        filters['sealant_shtapik'] = SealantShtapik.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'sealant_color',
                    'placeholder': 'Выберите цвет',
                    'label': 'цвет',
                    'data': serializer.data['sealant_color'],
                },
                {
                    'name': 'sealant_inside',
                    'placeholder': 'Выберите исполнение снаружи',
                    'label': 'Исполнение снаружи',
                    'data': serializer.data['sealant_inside'],
                },
                {
                    'name': 'sealant_outside',
                    'placeholder': 'Выберите исполнение внутри',
                    'label': 'Исполнение внутри',
                    'data': serializer.data['sealant_outside'],
                },
                {
                    'name': 'sealant_shtapik',
                    'placeholder': 'Выберите штапик',
                    'label': 'Штапик',
                    'data': serializer.data['sealant_shtapik'],
                },
            ]
        })


class ConstructorLowTidesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['windowsill'] = Windowsill.objects.all()
        filters['low_tides'] = LowTides.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'windowsill',
                    'placeholder': 'Выберите подоконник',
                    'label': 'Подоконники',
                    'data': serializer.data['windowsill'],
                },
                {'name': 'low_tides',
                 'placeholder': 'Выберите отливы',
                 'label': 'Отливы',
                 'data': serializer.data['low_tides'],
                 }
            ]
        })


class ConstructorLaminationsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['lamination_outside'] = LaminationOutside.objects.all()
        filters['lamination_inside'] = LaminationInside.objects.all()
        filters['profile_weight'] = ProfileWeight.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
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


class ConstructorAdditionOptionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['seal_outside'] = SealOutside.objects.all()
        filters['seal_internal'] = SealInternal.objects.all()
        filters['seal_color'] = SealColor.objects.all()
        filters['shpros'] = Shpros.objects.all()
        filters['shtapik'] = Shtapik.objects.all()
        filters['sash'] = Sash.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'seal_outside',
                    'placeholder': 'Выберите уплотнение снаружи',
                    'label': 'Уплотнение снаружи',
                    'data': serializer.data['seal_outside'],
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
                }
            ]
        })


class ConstructorMaterialAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
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
        filters['handles'] = OtherComplecation.objects.all()
        filters['locks'] = Locks.objects.all()
        filters['straight_connectors'] = StraightConnectors.objects.all()
        filters['supply_valve'] = SupplyValve.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
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
        filters['handles'] = OtherComplecation.objects.all()
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
        filters['handles'] = OtherComplecation.objects.all()
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




class WindowsillAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['windowsill'] = Windowsill.objects.all()
        filters['windowsill_color'] = WindowsillColor.objects.all()
        filters['windowsill_installation'] = WindowsillInstallation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'windowsill',
                    'placeholder': 'Выберите подоконник',
                    'label': 'Подоконник',
                    'data': serializer.data['windowsill'],
                },
                {
                    'name': 'windowsill_color',
                    'placeholder': 'Выберите цвет подоконника',
                    'label': 'Цвет подоконника',
                    'value': serializer.data['windowsill_color'],
                },
                {
                    'name': 'windowsill_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж подоконника',
                    'value': serializer.data['windowsill_installation'],
                }
            ]
        })


class CasingAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['casing'] = Casing.objects.all()
        filters['casing_color'] = CasingColor.objects.all()
        filters['casing_installation'] = CasingInstallation.objects.all()
        filters['casing_fastening'] = CasingFastening.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'casing',
                    'placeholder': 'Выберите наличник',
                    'label': 'Наличник',
                    'data': serializer.data['casing'],
                },
                {
                    'name': 'casing_color',
                    'placeholder': 'Выберите цвет наличника',
                    'label': 'Цвет наличника',
                    'value': serializer.data['casing_color'],
                },
                {
                    'name': 'casing_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж наличника',
                    'value': serializer.data['casing_installation'],
                },
                {
                    'name': 'casing_fastening',
                    'placeholder': 'Выберите крепление',
                    'label': 'Крепление',
                    'value': serializer.data['casing_fastening'],
                }
            ]
        })


class FlashingAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['flashing'] = Flashing.objects.all()
        filters['flashing_color'] = FlashingColor.objects.all()
        filters['flashing_installation'] = FlashingInstallation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'flashing',
                    'placeholder': 'Выберите нащельник',
                    'label': 'Нащельник',
                    'data': serializer.data['flashing'],
                },
                {
                    'name': 'flashing_color',
                    'placeholder': 'Выберите цвет нащельника',
                    'label': 'Цвет нащельника',
                    'value': serializer.data['flashing_color'],
                },
                {
                    'name': 'flashing_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж нащельника',
                    'value': serializer.data['flashing_installation'],
                }
            ]
        })


class InternalSlopeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['internal_slope'] = InternalSlope.objects.all()
        filters['internal_slope_color'] = InternalSlopeColor.objects.all()
        filters['internal_slope_installation'] = InternalSlopeInstallation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'internal_slope',
                    'placeholder': 'Выберите внутренние откосы',
                    'label': 'Внутренние откосы',
                    'data': serializer.data['internal_slope'],
                },
                {
                    'name': 'internal_slope_color',
                    'placeholder': 'Выберите цвет внутреннего откоса',
                    'label': 'Цвет внутренних откосов',
                    'value': serializer.data['internal_slope_color'],
                },
                {
                    'name': 'internal_slope_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж внутренних откосов',
                    'value': serializer.data['internal_slope_installation'],
                }
            ]
        })

class LowTidesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['low_tides'] = LowTides.objects.all()
        filters['low_tides_color'] = LowTidesColor.objects.all()
        filters['low_tides_installation'] = LowTidesInstallation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'low_tides',
                    'placeholder': 'Выберите отливы',
                    'label': 'Отлив',
                    'data': serializer.data['low_tides'],
                },
                {
                    'name': 'low_tides_color',
                    'placeholder': 'Выберите цвет отлива',
                    'label': 'Цвет отлива',
                    'value': serializer.data['low_tides_color'],
                },
                {
                    'name': 'low_tides_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж отлива',
                    'value': serializer.data['low_tides_installation'],
                }
            ]
        })

class VisorsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['visors'] = Visors.objects.all()
        filters['visors_color'] = VisorsColor.objects.all()
        filters['visors_installation'] = VisorsInstallation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'visors',
                    'placeholder': 'Выберите тип козырька',
                    'label': 'Тип козырька',
                    'data': serializer.data['visors'],
                },
                {
                    'name': 'visors_color',
                    'placeholder': 'Выберите цвет козырька',
                    'label': 'Цвет козырька',
                    'value': serializer.data['visors_color'],
                },
                {
                    'name': 'visors_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж козырька',
                    'value': serializer.data['visors_installation'],
                }
            ]
        })


class SlopesOfMetalAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['slopes_of_metal'] = SlopesOfMetal.objects.all()
        filters['slopes_of_metal_color'] = SlopesOfMetalColor.objects.all()
        filters['slopes_of_metal_installation'] = SlopesOfMetalInstallation.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'slope_of_metal',
                    'placeholder': 'Выберите тип откосов из металла',
                    'label': 'Тип откосов из металла',
                    'data': serializer.data['slopes_of_metal'],
                },
                {
                    'name': 'slope_of_metal_color',
                    'placeholder': 'Выберите цвет откосов из металла',
                    'label': 'Цвет откосов из металла',
                    'value': serializer.data['slopes_of_metal_color'],
                },
                {
                    'name': 'slope_of_metal_installation',
                    'placeholder': 'Выберите тип монтажа',
                    'label': 'Монтаж откосов из металла',
                    'value': serializer.data['slopes_of_metal_installation'],
                }
            ]
        })

class MountingMaterialsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['mounting_materials_type'] = MountingMaterialsType.objects.all()
        filters['mounting_materials_name'] = MountingMaterialsName.objects.all()

        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'mounting_materials_type',
                    'placeholder': 'Выберите тип монтажного материала',
                    'label': 'Тип монтажного материала',
                    'data': serializer.data['mounting_materials_type'],
                },
                {
                    'name': 'mounting_materials_name',
                    'placeholder': 'Выберите наименование монтажного материала',
                    'label': 'Наименование монтажного материала',
                    'value': serializer.data['mounting_materials_name'],
                }
            ]
        })


class WorksAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {'works': Works.objects.all()}
        serializer = ConstructorSerializer(filters)
        return Response({
            'data': [
                {
                    'name': 'works',
                    'placeholder': 'Выберите работы',
                    'label': 'Работы',
                    'data': serializer.data['works'],
                },

            ]
        })
