from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .models import *
from .utils import *


# Create your views here.

class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"


def home(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "GET":
        try:
            id_order = request.GET.get('id_order')
            order = Order.objects.get(pk=id_order)
            order.delete()
        except:
            pass
    if request.method == 'POST':
        address = request.POST.get('address')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        new_order = Order.objects.create(user=user, address=address, name=name, phone=phone, date=date)
        new_order.save()

        context = {
            'order': new_order,

        }
        return render(request, 'measurer_window/order_detail.html', context)

    orders = Order.objects.filter(user=user)

    context = {
        'test': 'test',
        'orders': orders,
    }
    return render(request, 'measurer_window/home.html', context)


def update_order(request, pk):
    address = request.POST.get('order_address')
    name = request.POST.get('order_name')
    phone = request.POST.get('order_phone')
    date = request.POST.get('order_date')
    status = request.POST.get('order_status')
    order = Order.objects.get(pk=pk)
    order.address = address
    order.name = name
    order.phone = phone
    order.date = date
    order.status = status
    order.save()


def create_windowsill_calc(request, pk):
    id_windowsill = request.POST.get('id_windowsill')
    windowsill_length = request.POST.get('windowsill_length')
    windowsill_width = request.POST.get('windowsill_width')
    windowsill_count = request.POST.get('windowsill_count')
    calc_windowsill(order_id=pk, windowsill_id=id_windowsill, width=windowsill_width, length=windowsill_length,
                    count=windowsill_count)


def create_windowsill_complect_calc(request, pk):
    id_low_tides = request.POST.get('id_low_tides_complect')
    low_tides_count = request.POST.get('low_tides_count')
    calc_low_tides_complect(order_id=pk, low_tides=id_low_tides, low_tides_count=low_tides_count)


def create_low_tides_calc(request, pk):
    low_tides = request.POST.get('id_low_tides')
    low_tides_length = request.POST.get('low_tides_length')
    low_tides_width = request.POST.get('low_tides_width')
    low_tides_count = request.POST.get('low_tides_count')
    calc_low_tides(order_id=pk, low_tides_id=low_tides, width=low_tides_width, length=low_tides_length,
                   count=low_tides_count)


def create_low_tides_complect_calc(request, pk):
    id_low_tides = request.POST.get('id_low_tides_complect')
    low_tides_count = request.POST.get('low_tides_count')
    calc_low_tides_complect(order_id=pk, low_tides=id_low_tides, low_tides_count=low_tides_count)


def delete_windowsill_calc(request):
    id_windowsill_calc = request.GET.get('id_windowsill_calc')
    windowsill_calc = WindowsillCalc.objects.get(pk=id_windowsill_calc)
    windowsill_calc.delete()


def delete_windowsill_complect_calc(request):
    id_windowsill_complect_calc = request.GET.get('id_windowsill_complect_calc')
    windowsill_complect_calc = WindowsillComplectCalc.objects.get(pk=id_windowsill_complect_calc)
    windowsill_complect_calc.delete()

def delete_low_tides_calc(request):
    id_low_tides_calc = request.GET.get('id_low_tides_calc')
    low_tides_calc = LowTidesCalc.objects.get(pk=id_low_tides_calc)
    low_tides_calc.delete()


def delete_low_tides_complect_calc(request):
    id_low_tides_complect_calc = request.GET.get('id_low_tides_complect_calc')
    low_tides_complect_calc = LowTidesComplectCalc.objects.get(pk=id_low_tides_complect_calc)
    low_tides_complect_calc.delete()

def order(request, pk):
    if request.method == "GET":
        try:
            delete_windowsill_calc(request)
        except:
            print('пытался удалить windowsill_calc')
        try:
            delete_windowsill_complect_calc(request)
        except:
            print('пытался удалить windowsill_complect_calc')

        try:
            delete_low_tides_calc(request)
        except:
            print('пытался удалить low_tides_calc')
        try:
            delete_low_tides_complect_calc(request)
        except:
            print('пытался удалить low_tides_complect_calc')

    if request.method == 'POST':
        try:
            create_windowsill_calc(request, pk)
        except:
            print('пытался создать windowsill')
        try:
            create_windowsill_complect_calc()
        except:
            print('пытался создать windowsill complect')

        try:
            create_low_tides_calc(request, pk)
        except:
            print('пытался создать lowtides')
        try:
            create_windowsill_complect_calc(request,pk)
        except:
            print('пытался создать low_tides complect')
        try:
            update_order(request, pk)
        except:
            print('пытался обновить статус')

    calc_order(order_id=pk)
    order = Order.objects.get(pk=pk)

    windowsill = Windowsill.objects.filter(unit=1).order_by('-id')
    windowsill_complect = Windowsill.objects.filter(unit=2).order_by('-id')
    windowsill_calc = WindowsillCalc.objects.filter(order_id=pk).order_by('-id')
    windowsill_complect_calc = WindowsillComplectCalc.objects.filter(order_id=pk).order_by('-id')

    low_tides = LowTides.objects.filter(unit=1).order_by('-id')
    low_tides_complect = LowTides.objects.filter(unit=2).order_by('-id')
    low_tides_calc = LowTidesCalc.objects.filter(order_id=pk).order_by('-id')
    low_tides_complect_calc = LowTidesComplectCalc.objects.filter(order_id=pk).order_by('-id')


    context = {
        'order': order,

        'windowsill': windowsill,
        'windowsill_complect': windowsill_complect,
        'windowsill_complect_calc': windowsill_complect_calc,

        'lowtides': low_tides,
        'low_tides_complect': low_tides_complect,
        'low_tides_complect_calc': low_tides_complect_calc,

        'windowsill_calc': windowsill_calc,
        'low_tides_calc': low_tides_calc,

    }
    return render(request, 'measurer_window/order_detail.html', context)
