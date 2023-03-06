from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from .utils import *
from .serializer import *
from .forms import *
def index(request):
    if request.method == "GET":
        date = request.GET.get('calendar')
        if date is None or date == "":
            date = datetime.now().date()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        date = request.GET.get('calendar')
        if date is None or date == "":
            date = datetime.now().date()
        pk = request.POST.get('pk')
        client = request.POST.get('client')
        address = request.POST.get('address')
        number = request.POST.get('number')
        time = request.POST.get('time')
        date_measurement = request.POST.get('calendarMeasurement')
        comment = request.POST.get('comment')
        status = request.POST.get('select')
        final_amount = request.POST.get('final_amount')
        executor = request.POST.get('selectMeasurers')
        try:
            file = request.FILES['image']
        except:
            file = None

        update_log(request=request,
                   pk=pk, client=client,
                   address=address,
                   number=number,
                   time=time,
                   date=date_measurement,
                   comment=comment,
                   status=status,
                   final_amount=final_amount,
                   file=file,
                   executor=executor, )

        update_measurement(request=request,
                           pk=pk, client=client,
                           address=address,
                           number=number,
                           time=time,
                           date=date_measurement,
                           comment=comment,
                           status=status,
                           final_amount=final_amount,
                           file=file,
                           executor=executor,
                           )

        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    # if request.POST.get('check_measurement'):
    #     request.session.clear()
    #     print('ez blyat')
    context = {
        'curr_measurements': get_measurements(request, date),
        'form': form,
        # 'agreements': agreements,
        'measurers': get_measurers(),
        'calendar': get_calendar(),
        'all_measurements': get_all_measurements(request),
    }
    return render(request, 'measurer/order_detail.html', context)


class MeasurementViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Measurement.objects.all()
        miscalculation = get_object_or_404(queryset, pk=pk)
        serializer = MeasurementSerializer(miscalculation)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})

