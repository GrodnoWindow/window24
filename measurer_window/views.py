from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .forms import *
from .models import *
from .utils import *


# Create your views here.

class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"


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

        form_windowsill_calc = WindowsillCalcForm(request.POST)
        if form_windowsill_calc.is_valid():
            windowsill = form_windowsill_calc.cleaned_data.get("windowsill")
            length = form_windowsill_calc.cleaned_data.get("length")
            windowsill_width = form_windowsill_calc.cleaned_data.get("width")
            count = form_windowsill_calc.cleaned_data.get("count")
            calc_windowsill(order_id=pk, windowsill=windowsill, windowsill_width=windowsill_width, length=length,
                            count=count)
            return redirect('order', pk=pk)

        form_windowsill_complect_calc = WindowsillComplectCalcForm(request.POST)
        if form_windowsill_complect_calc.is_valid():
            windowsill = form_windowsill_complect_calc.cleaned_data.get("windowsill")
            count = form_windowsill_complect_calc.cleaned_data.get("count")
            calc_windowsill_complect(order_id=pk, windowsill=windowsill, count=count)
            return redirect('order', pk=pk)

        form_low_tides_calc = LowTidesCalcForm(request.POST)
        if form_low_tides_calc.is_valid():
            low_tides = form_low_tides_calc.cleaned_data.get("low_tides")
            length = form_low_tides_calc.cleaned_data.get("length")
            width = form_low_tides_calc.cleaned_data.get("width")
            count = form_low_tides_calc.cleaned_data.get("count")
            calc_low_tides(order_id=pk, low_tides=low_tides, width=width, length=length,
                           count=count)
            return redirect('order', pk=pk)

        form_low_tides_complect_calc = LowTidesComplectCalcForm(request.POST)
        if form_low_tides_complect_calc.is_valid():
            low_tides = form_low_tides_complect_calc.cleaned_data.get("low_tides")
            count = form_low_tides_complect_calc.cleaned_data.get("count")
            calc_low_tides_complect(order_id=pk, low_tides=low_tides, count=count)
            return redirect('order', pk=pk)

        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = form_order.save()
            order.save()
            return redirect('order', pk=pk)


    calc_order(order_id=pk)
    order = Order.objects.get(pk=pk)

    windowsill_calc = WindowsillCalc.objects.filter(order_id=pk).order_by('-id')

    low_tides_calc = LowTidesCalc.objects.filter(order_id=pk).order_by('-id')

    form_order = OrderForm(initial={
        'address': order.address,
        'name': order.name,
        'phone': order.phone,
        'date': order.date,
        'status': order.status,

    })
    form_windowsill_calc = WindowsillCalcForm(initial={'count': 1})
    form_windowsill_complect_calc = WindowsillComplectCalcForm(initial={'count': 1})
    windowsill_complect_calc = WindowsillComplectCalc.objects.filter(order_id=pk)

    form_low_tides_calc = LowTidesCalcForm(initial={'count': 1})
    form_low_tides_complect_calc = LowTidesComplectCalcForm(initial={'count': 1})
    low_tides_complect_calc = LowTidesComplectCalc.objects.filter(order_id=pk)

    context = {
        'order': order,

        'form_order': form_order,

        'form_windowsill_calc': form_windowsill_calc,
        'form_windowsill_complect_calc': form_windowsill_complect_calc,
        'windowsill_calc': windowsill_calc,
        'windowsill_complect_calc': windowsill_complect_calc,

        'form_low_tides_calc': form_low_tides_calc,
        'form_low_tides_complect_calc': form_low_tides_complect_calc,
        'low_tides_calc': low_tides_calc,
        'low_tides_complect_calc': low_tides_complect_calc,

        #
        # 'lowtides': low_tides,
        # 'low_tides_complect': low_tides_complect,


    }
    return render(request, 'measurer_window/order_detail.html', context)


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
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = form_order.save()
            order.user = user
            order.save()
            context = {
                'order': order,
            }
            # return render(request, 'measurer_window/order_detail.html', context)
            return redirect('order', pk=order.pk)

    orders = Order.objects.filter(user=user).order_by('-pk')
    form_order = OrderForm(initial={'phone': "+375"})
    context = {
        'form_order': form_order,
        'orders': orders,
    }
    return render(request, 'measurer_window/home.html', context)
