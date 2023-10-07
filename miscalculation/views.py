import json
import datetime

import coreschema as coreschema
from django.core.serializers import serialize
from django.http import FileResponse
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

import calculation
from calculation.serializer import WindowsillCalcSerializer
from constructor.models import LowTides, LowTidesColor, Flashing, FlashingColor, Visors, VisorsColor, Casing, \
    CasingColor, CasingFastening, SlopesOfMetal, SlopesOfMetalColor, InternalSlope, InternalSlopeColor, \
    MountingMaterialsName, Works, AdditionalProfile, ConnectionProfile, OtherComplectationProfile
from constructor.serializer import ProductTypeSerializer, WindowsillSerializer
from .serializer import MiscalculationSerializer, CommercialOfferSerializer, HideCostSerializer
from .models import *
from .utils import *
from config.pagination import CustomPagination
from django.core import serializers


class MiscalculationViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Miscalculation.objects.all()
    serializer_class = MiscalculationSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        miscalculation = Miscalculation.objects.create(created_time=datetime.datetime.now(),
                                                       last_update_time=datetime.datetime.now())
        miscalculation.author = request.user.username

        try:
            for constructors in request.data['constructors']:
                miscalculation.constructors.add(constructors)
            for constructors in miscalculation.constructors.all():
                miscalculation.sum += constructors.price_constructor
        except:
            pass
        try:
            miscalculation.status = request.data['status']
        except:
            pass
        try:
            miscalculation.offer = request.data['offer']
        except:
            pass

        miscalculation.save()
        serializer = MiscalculationSerializer(miscalculation)

        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Miscalculation.objects.all()
        miscalculation = get_object_or_404(queryset, pk=pk)
        serializer = MiscalculationSerializer(miscalculation)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        miscalculation_id = instance.id
        miscalculation = Miscalculation.objects.get(pk=miscalculation_id)
        miscalculation.sum = 0
        try:
            miscalculation.constructors.clear()  # Очистка связанных конструкторов

            for constructor_id in request.data.get('constructors', []):
                constructor = Constructor.objects.get(pk=constructor_id)
                miscalculation.constructors.add(constructor)

            # Подсчет суммы
            sum_price = sum(constructor.price_constructor for constructor in miscalculation.constructors.all())
            miscalculation.sum = sum_price

            # Обновление остальных полей
            miscalculation.status = request.data['status']
            miscalculation.author = request.user.username

            miscalculation.save()

            serializer = MiscalculationSerializer(miscalculation)
            return Response({"data": serializer.data})
        except Miscalculation.DoesNotExist:
            return Response({'error': 'Miscalculation not found.'}, status=status.HTTP_404_NOT_FOUND)


class CommercialOfferViewSet(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin, GenericViewSet):
    queryset = Miscalculation.objects.all()
    serializer_class = MiscalculationSerializer

    def retrieve(self, request, pk=None):
        queryset = Miscalculation.objects.all()
        miscalculation = get_object_or_404(queryset, pk=pk)

        output_data = []
        for constructor in miscalculation.constructors.all():
            import base64
            from PIL import Image
            import io

            base64_image = constructor.final_image
            base64_data = base64_image.replace("data:image/png;base64,", "")
            image_data = base64.b64decode(base64_data)

            image = Image.open(io.BytesIO(image_data))
            image.save(f"{MEDIA_ROOT}/offers/constructor_{constructor.pk}_image.png")
            constructor.final_image_url = f"constructor_{constructor.pk}_image.png"
            constructor.save()
            data = {}
            if constructor.final_image_url:
                data["URL изображения"] = constructor.final_image_url
            if constructor.product_type:
                data["Тип изделия"] = constructor.product_type.name
            if constructor.name:
                data["Имя"] = constructor.name

            if constructor.context:
                data["Контекст"] = constructor.context

            if constructor.stb_info:
                data["СТБ_название"] = constructor.stb_info

            if constructor.aggregate:
                data["Заполнитель"] = constructor.aggregate.name
            if constructor.window_calc:
                data["Цена изделия"] = constructor.window_calc.price_output

            if constructor.shtapik:
                data["Штапик"] = constructor.shtapik.name

            if constructor.sash:
                data["Створка"] = constructor.sash.name

            if constructor.gorbylki:
                data["Горбыльки"] = constructor.gorbylki.name

            if constructor.handles:
                data["Ручки"] = constructor.handles.name

            if constructor.door:
                door_data = {}
                door_data["Тип изделия"] = constructor.door.product_type.name
                door_data["Со штульпом"] = constructor.door.shtulp
                door_data["Открывание"] = constructor.door.opening.name
                door_data["Замок"] = constructor.door.lock.name
                door_data["Дверные ручки"] = constructor.door.handle.name
                door_data["Дверные петли"] = constructor.door.door_hinges.name
                door_data["Цилиндр"] = constructor.door.cylinder.name
                door_data["Ограничитель открывания"] = constructor.door.opening_limiter.name
                data["Дверь"] = door_data

            # if constructor.connection_profile:
            #     profile_data = {}
            #     profile_data["Профиль"] = constructor.connection_profile.profile.name
            #     profile_data["Артикул"] = constructor.connection_profile.connection_article.name
            #     profile_data["Название соединителя"] = constructor.connection_profile.name.name
            #     profile_data["Цвет внутри"] = constructor.connection_profile.color_inside.name
            #     profile_data["Цвет снаружи"] = constructor.connection_profile.color_outside.name
            #     profile_data["Длина"] = constructor.connection_profile.length
            #     profile_data["Цена"] = constructor.connection_profile.price
            #
            #     data["Соединительный профиль"] = profile_data

            # if constructor.additional_profile:
            #     profile_data = {}
            #     profile_data["Артикул"] = constructor.additional_profile.additional_article.name
            #     profile_data["Ширина"] = constructor.additional_profile.width
            #     profile_data["Цена"] = constructor.additional_profile.price
            #
            #     data["Доборный профиль"] = profile_data

            # if constructor.other_complectation:
            #     data["Прочее комплектующие"] = constructor.other_complectation.name

            if constructor.sealant:
                sealant_data = {}
                sealant_data["Цвет уплотнителя"] = constructor.sealant.sealant_color.name
                sealant_data["Исполнение снаружи"] = constructor.sealant.sealant_inside.name
                sealant_data["Исполнение внутри"] = constructor.sealant.sealant_outside.name
                sealant_data["Штапик уплотнителя"] = constructor.sealant.sealant_shtapik.name
                data["Уплотнитель"] = sealant_data

            if constructor.lamination:
                lamination_data = {}
                lamination_data["Тип ламинации"] = constructor.lamination.type_lamination.name
                lamination_data["Вид ламинации"] = constructor.lamination.type_lamination1.name
                lamination_data["Исполнение внутри"] = constructor.lamination.seal_internal.name
                lamination_data["Исполнение снаружи"] = constructor.lamination.seal_outside.name
                lamination_data["Исполнение основы детали"] = constructor.lamination.seal_basic.name
                data["Ламинация"] = lamination_data

            if hasattr(constructor, 'additional_profile_calc') and constructor.additional_profile_calc.exists():
                additional_profile_data = []
                for el in constructor.additional_profile_calc.all():
                    additional_profile_model = AdditionalProfile.objects.get(pk=el.additional_profile_id)
                    additional_profile = {}
                    additional_profile['Артикул'] = additional_profile_model.additional_article.name
                    additional_profile['Ширина'] = additional_profile_model.additional_width.name
                    additional_profile['Ширина1'] = additional_profile_model.additional_width.name
                    additional_profile['Ламинация'] = additional_profile_model.additional_lamination.name
                    additional_profile['Количество'] = el.count
                    additional_profile['Цена'] = el.price_output
                    additional_profile_data.append(additional_profile)

                data["Доборные_Профиля"] = additional_profile_data

            if hasattr(constructor, 'connection_profile_calc') and constructor.connection_profile_calc.exists():
                connection_profile_data = []
                for el in constructor.connection_profile_calc.all():
                    connection_profile_model = ConnectionProfile.objects.get(pk=el.connection_profile_id)
                    connection_profile = {}
                    connection_profile['Артикул'] = connection_profile_model.connection_article.name
                    connection_profile['Ширина'] = connection_profile_model.connection_width.name
                    connection_profile['Ширина1'] = connection_profile_model.connection_width.name
                    connection_profile['Ламинация'] = connection_profile_model.connection_lamination.name
                    connection_profile['Количество'] = el.count
                    connection_profile['Цена'] = el.price_output
                    connection_profile_data.append(connection_profile)

                data["Соединительные_Профиля"] = connection_profile_data

            if hasattr(constructor, 'other_complectation_profile_calc') and constructor.other_complectation_profile_calc.exists():
                other_complectation_profile_data = []
                for el in constructor.other_complectation_profile_calc.all():
                    other_complectation_profile_model = OtherComplectationProfile.objects.get(pk=el.other_complectation_id)
                    other_complectation_profile = {}
                    other_complectation_profile['Артикул'] = other_complectation_profile_model.additional_article.name
                    other_complectation_profile['Ширина'] = other_complectation_profile_model.additional_width.name
                    other_complectation_profile['Ширина1'] = other_complectation_profile_model.additional_width.name
                    other_complectation_profile['Ламинация'] = other_complectation_profile_model.additional_lamination.name
                    other_complectation_profile['Количество'] = el.count
                    other_complectation_profile['Цена'] = el.price_output
                    other_complectation_profile_data.append(other_complectation_profile)

                data["Доп_Комплект_Профиля"] = other_complectation_profile_data

            if hasattr(constructor, 'windowsills_calc') and constructor.windowsills_calc.exists():
                windowsill_data = []
                for el in constructor.windowsills_calc.all():
                    windowsill_model = Windowsill.objects.get(pk=el.windowsill_id)
                    windowsill_color = WindowsillColor.objects.get(pk=el.color_id)
                    windowsill = {}
                    windowsill['Название'] = windowsill_model.name
                    windowsill['Цвет'] = windowsill_color.name
                    windowsill['Установка'] = el.installation_id
                    windowsill['Заглушка'] = el.plug
                    windowsill['Соединитель'] = el.connector
                    windowsill['Ширина'] = el.width
                    windowsill['Длинна'] = el.length
                    windowsill['Количество'] = el.count
                    windowsill['Цена'] = el.price_output
                    windowsill['Поставщик'] = windowsill_model.windowsill_provider.name
                    windowsill_data.append(windowsill)

                data["Подоконники"] = windowsill_data

            if hasattr(constructor, 'lowtides_calc') and constructor.lowtides_calc.exists():
                lowtides_data = []
                for el in constructor.lowtides_calc.all():
                    lowtides_model = LowTides.objects.get(pk=el.low_tides_id)
                    lowtides_color = LowTidesColor.objects.get(pk=el.color_id)
                    lowtides = {}
                    lowtides['Название'] = lowtides_model.name
                    lowtides['Цвет'] = lowtides_color.name
                    lowtides['Установка'] = el.installation_id
                    lowtides['Заглушка'] = el.plug
                    lowtides['Ширина'] = el.width
                    lowtides['Длинна'] = el.length
                    lowtides['Количество'] = el.count
                    lowtides['Цена'] = el.price_output
                    lowtides['Поставщик'] = lowtides_model.low_tides_provider.name
                    lowtides_data.append(lowtides)

                data["Отливы"] = lowtides_data

            if hasattr(constructor, 'flashing_calc') and constructor.flashing_calc.exists():
                flashing_data = []
                for el in constructor.flashing_calc.all():
                    flashing_model = Flashing.objects.get(pk=el.flashing_id)
                    flashing_color = FlashingColor.objects.get(pk=el.color_id)
                    flashing = {}
                    flashing['Название'] = flashing_model.name
                    flashing['Цвет'] = flashing_color.name
                    flashing['Установка'] = el.installation_id
                    flashing['Ширина'] = el.width
                    flashing['Длинна'] = el.length
                    flashing['Количество'] = el.count
                    flashing['Цена'] = el.price_output
                    flashing['Поставщик'] = flashing_model.flashing_provider.name
                    flashing_data.append(flashing)

                data["Нащельники"] = flashing_data

            if hasattr(constructor, 'visors_calc') and constructor.visors_calc.exists():
                visors_data = []
                for el in constructor.visors_calc.all():
                    visors_model = Visors.objects.get(pk=el.visors_id)
                    visors_color = VisorsColor.objects.get(pk=el.color_id)
                    visors = {}
                    visors['Название'] = visors_model.name
                    visors['Цвет'] = visors_color.name
                    visors['Установка'] = el.installation_id
                    visors['Ширина'] = el.width
                    visors['Длинна'] = el.length
                    visors['Количество'] = el.count
                    visors['Цена'] = el.price_output
                    visors['Поставщик'] = visors_model.visors_provider.name
                    visors_data.append(visors)

                data["Козырьки"] = visors_data

            if hasattr(constructor, 'casing_calc') and constructor.casing_calc.exists():
                casing_data = []
                for el in constructor.casing_calc.all():
                    casing_model = Casing.objects.get(pk=el.casing_id)
                    casing_color = CasingColor.objects.get(pk=el.color_id)
                    fastening = CasingFastening.objects.get(pk=el.fastening_id)
                    casing = {}
                    casing['Название'] = casing_model.name
                    casing['Цвет'] = casing_color.name
                    casing['Установка'] = el.installation_id
                    casing['Крепление'] = fastening.name
                    casing['Ширина'] = el.width
                    casing['Длинна'] = el.length
                    casing['Количество'] = el.count
                    casing['Цена'] = el.price_output
                    casing['Поставщик'] = casing_model.casing_provider.name
                    casing_data.append(casing)

                data["Наличники"] = casing_data

            if hasattr(constructor, 'slopes_of_metal_calc') and constructor.slopes_of_metal_calc.exists():
                slopes_of_metal_data = []
                for el in constructor.slopes_of_metal_calc.all():
                    slopes_of_metal_model = SlopesOfMetal.objects.get(pk=el.slopes_of_metal_id)
                    slopes_of_metal_color = SlopesOfMetalColor.objects.get(pk=el.color_id)
                    slopes_of_metal = {}
                    slopes_of_metal['Название'] = slopes_of_metal_model.name
                    slopes_of_metal['Цвет'] = slopes_of_metal_color.name
                    slopes_of_metal['Установка'] = el.installation_id

                    slopes_of_metal['Ширина'] = el.width
                    slopes_of_metal['Длинна'] = el.length
                    slopes_of_metal['Ширина_1'] = el.width_1
                    slopes_of_metal['Ширина_2'] = el.width_2
                    slopes_of_metal['Ширина_3'] = el.width_3
                    slopes_of_metal['Ширина_4'] = el.width_4
                    slopes_of_metal['Откос_мп'] = el.linear_meter
                    slopes_of_metal['Откос_м2'] = el.square_meter

                    slopes_of_metal['Ширина_Замка'] = el.lock_width
                    slopes_of_metal['Длинна_Замка'] = el.lock_length
                    slopes_of_metal['Ширина_Замка_1'] = el.lock_width_1
                    slopes_of_metal['Ширина_Замка_2'] = el.lock_width_2
                    slopes_of_metal['Ширина_Замка_3'] = el.lock_width_3
                    slopes_of_metal['Ширина_Замка_4'] = el.lock_width_4
                    slopes_of_metal['Замок_мп'] = el.linear_meter_lock
                    slopes_of_metal['Замок_м2'] = el.square_meter_lock
                    slopes_of_metal['Замок_Цена'] = el.price_lock

                    slopes_of_metal['Ширина_Отлива'] = el.low_tides_width
                    slopes_of_metal['Длинна_Отлива'] = el.low_tides_length
                    slopes_of_metal['Ширина_Отлива_1'] = el.low_tides_width_1
                    slopes_of_metal['Ширина_Отлива_2'] = el.low_tides_width_2
                    slopes_of_metal['Ширина_Отлива_3'] = el.low_tides_width_3
                    slopes_of_metal['Ширина_Отлива_4'] = el.low_tides_width_4
                    slopes_of_metal['Отлив_мп'] = el.linear_meter_low_tides
                    slopes_of_metal['Отлив_м2'] = el.square_meter_low_tides
                    slopes_of_metal['Отлив_Цена'] = el.price_low_tides

                    slopes_of_metal['Количество'] = el.count
                    slopes_of_metal['Количество_Замков'] = el.lock_count
                    slopes_of_metal['Цена'] = el.price_output
                    slopes_of_metal['Поставщик'] = slopes_of_metal_model.slopes_of_metal_provider.name
                    slopes_of_metal_data.append(slopes_of_metal)

                data["Откосы из металла"] = slopes_of_metal_data

            if hasattr(constructor, 'internal_slope_calc') and constructor.internal_slope_calc.exists():

                internal_slope_data = []
                for el in constructor.internal_slope_calc.all():
                    internal_slope_model = InternalSlope.objects.get(pk=el.internal_slope_id)
                    internal_slope_color = InternalSlopeColor.objects.get(pk=el.color_id)
                    internal_slope = {}

                    index = internal_slope_model.type
                    if index == 0:
                        internal_slope['Тип'] = 'Кюнель'
                    elif index == 1:
                        internal_slope['Тип'] = 'ПВХ'

                    internal_slope['Название'] = internal_slope_model.name
                    internal_slope['Цвет'] = internal_slope_color.name
                    internal_slope['Установка'] = el.installation_id
                    internal_slope['Ширина'] = el.width
                    internal_slope['Длинна'] = el.length
                    internal_slope['Количество'] = el.count
                    internal_slope['Цена'] = el.price_output
                    internal_slope['Высота_1'] = el.height_1
                    internal_slope['Высота_2'] = el.height_2
                    internal_slope['Стартовый_Профиль'] = el.start_profile_length
                    internal_slope['Наличник_Профиль'] = el.casing_length
                    internal_slope['Колво_крышек'] = el.lid_count
                    internal_slope['Колво_защелок'] = el.latch_count
                    internal_slope['Колво_f'] = el.f_count
                    internal_slope['Поставщик'] = internal_slope_model.internal_slope_provider.name
                    internal_slope_data.append(internal_slope)

                data["Внутренние откосы"] = internal_slope_data

            if hasattr(constructor, 'mounting_materials_calc') and constructor.mounting_materials_calc.exists():
                mounting_materials_data = []
                for el in constructor.mounting_materials_calc.all():
                    mounting_materials_model = MountingMaterialsName.objects.get(pk=el.mounting_materials_id)
                    mounting_materials = {}
                    mounting_materials['Название'] = mounting_materials_model.name
                    mounting_materials['Количество'] = el.count
                    mounting_materials['Цена'] = el.price_output
                    mounting_materials_data.append(mounting_materials)

                data["Монтажные материалы"] = mounting_materials_data

            if hasattr(constructor, 'works') and constructor.works.exists():
                works_data = []
                for el in constructor.works.all():
                    works = {}
                    works['Название'] = el.name
                    works['Цена'] = el.price
                    works_data.append(works)

                data["Работы"] = works_data

            if constructor.price_constructor:
                data["Сумма конструктора"] = str(constructor.price_constructor)

            output_data.append({"Конструктор": data})

        return Response({"Конструкторы": output_data, "Сумма просчета": miscalculation.sum})


class FileView(APIView):
    def get(self, request, file_name):
        file_path = os.path.join(MEDIA_ROOT, 'offers', file_name)

        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='image/png')
        else:
            return Response({'error': 'File not found'}, status=404)


class MiscalculationAddHideCostAPIView(APIView):
    serializer_class = HideCostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        add_hide_cost_miscalculation(request.data['pk'], request.data['cost'])
        miscalculation = Miscalculation.objects.get(pk=request.data['pk'])
        serializer = MiscalculationSerializer(miscalculation)
        return Response({"data": serializer.data})


class MiscalculationMinusHideCostAPIView(APIView):
    serializer_class = HideCostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        minus_hide_cost_miscalculation(request.data['pk'], request.data['cost'])
        miscalculation = Miscalculation.objects.get(pk=request.data['pk'])
        serializer = MiscalculationSerializer(miscalculation)
        return Response({"data": serializer.data})
