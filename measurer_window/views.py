from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .forms import *
from .models import *
from .utils import *


# Create your views here.

class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"


def order(request, pk, form):
    user = User.objects.get(username=request.user.username)

    if request.method == "GET":
        try:
            WindowsillCalc.objects.get(pk=request.GET.get('id_windowsill_calc')).delete()
            form = 'windowsill_calc'
        except:
            pass
        try:
            LowTidesCalc.objects.get(pk=request.GET.get('id_low_tides_calc')).delete()
            form = 'low_tides_calc'
        except:
            pass
        try:
            VisorsCalc.objects.get(pk=request.GET.get('id_visors_calc')).delete()
            form = 'visors_calc'
        except:
            pass
        try:
            FlashingCalc.objects.get(pk=request.GET.get('id_flashing_calc')).delete()
            form = 'flashing_calc'
        except:
            pass
        try:
            CasingCalc.objects.get(pk=request.GET.get('id_casing_calc')).delete()
            form = 'casing_calc'
        except:
            pass
        try:
            SlopesOfMetalCalc.objects.get(pk=request.GET.get('id_slopes_of_metal_calc')).delete()
            form = 'slopes_of_metal_calc'
        except:
            pass
        try:
            InternalSlopesCalc.objects.get(pk=request.GET.get('id_internal_slopes_calc')).delete()
            form = 'internal_slopes_calc'
        except:
            pass
        try:
            MountingMaterialsCalc.objects.get(pk=request.GET.get('id_mounting_materials_calc')).delete()
            form = 'mounting_materials_calc'
        except:
            pass
        try:
            WorksCalc.objects.get(pk=request.GET.get('id_works_calc')).delete()
            form = 'works_calc'
        except:
            pass
    if request.method == 'POST':
        form_windowsill_calc = WindowsillCalcForm(request.POST)
        if form_windowsill_calc.is_valid():
            windowsill = form_windowsill_calc.cleaned_data.get("windowsill")
            windowsill_color = form_windowsill_calc.cleaned_data.get("windowsill_color")
            length = form_windowsill_calc.cleaned_data.get("length")
            windowsill_width = form_windowsill_calc.cleaned_data.get("windowsill_width")
            windowsill_count = form_windowsill_calc.cleaned_data.get("windowsill_count")
            windowsill_plug = form_windowsill_calc.cleaned_data.get("windowsill_plug")
            windowsill_plug_count = form_windowsill_calc.cleaned_data.get("windowsill_plug_count")
            windowsill_connection = form_windowsill_calc.cleaned_data.get("windowsill_connection")
            windowsill_connection_count = form_windowsill_calc.cleaned_data.get("windowsill_connection_count")
            calc_windowsill(order_id=pk, windowsill=windowsill, windowsill_width=windowsill_width,
                            windowsill_color=windowsill_color, length=length,
                            windowsill_count=windowsill_count,
                            windowsill_plug=windowsill_plug, windowsill_plug_count=windowsill_plug_count,
                            windowsill_connection=windowsill_connection,
                            windowsill_connection_count=windowsill_connection_count)
            # return redirect('order', pk=pk, form='windowsill_calc')

        form_low_tides_calc = LowTidesCalcForm(request.POST)
        if form_low_tides_calc.is_valid():
            low_tides = form_low_tides_calc.cleaned_data.get("low_tides")
            low_tides_color = form_low_tides_calc.cleaned_data.get("low_tides_color")
            low_tides_type = form_low_tides_calc.cleaned_data.get("low_tides_type")
            length = form_low_tides_calc.cleaned_data.get("length")
            low_tides_width = form_low_tides_calc.cleaned_data.get("low_tides_width")
            low_tides_count = form_low_tides_calc.cleaned_data.get("low_tides_count")
            low_tides_plug = form_low_tides_calc.cleaned_data.get("low_tides_plug")
            low_tides_plug_count = form_low_tides_calc.cleaned_data.get("low_tides_plug_count")
            low_tides_connection = form_low_tides_calc.cleaned_data.get("low_tides_connection")
            low_tides_connection_count = form_low_tides_calc.cleaned_data.get("low_tides_connection_count")
            calc_low_tides(order_id=pk, low_tides=low_tides, low_tides_width=low_tides_width,
                           low_tides_type=low_tides_type,
                           low_tides_color=low_tides_color, length=length,
                           low_tides_count=low_tides_count,
                           low_tides_plug=low_tides_plug, low_tides_plug_count=low_tides_plug_count,
                           low_tides_connection=low_tides_connection,
                           low_tides_connection_count=low_tides_connection_count)
            return redirect('order', pk=pk, form='low_tides_calc')

        form_visors_calc = VisorsCalcForm(request.POST)
        if form_visors_calc.is_valid():
            visors = form_visors_calc.cleaned_data.get("visors")
            visors_color = form_visors_calc.cleaned_data.get("visors_color")
            length = form_visors_calc.cleaned_data.get("length")
            width = form_visors_calc.cleaned_data.get("width")
            count = form_visors_calc.cleaned_data.get("count")
            calc_visors(order_id=pk, visors=visors, visors_color=visors_color, width=width, length=length,
                        count=count)
            return redirect('order', pk=pk, form='visors_calc')

        form_flashing_calc = FlashingCalcForm(request.POST)
        if form_flashing_calc.is_valid():
            flashing = form_flashing_calc.cleaned_data.get("flashing")
            flashing_color = form_flashing_calc.cleaned_data.get("flashing_color")
            length = form_flashing_calc.cleaned_data.get("length")
            width = form_flashing_calc.cleaned_data.get("width")
            count = form_flashing_calc.cleaned_data.get("count")
            calc_flashing(order_id=pk, flashing=flashing, flashing_color=flashing_color, width=width, length=length,
                          count=count)
            return redirect('order', pk=pk, form='flashing_calc')

        form_casing_calc = CasingCalcForm(request.POST)
        if form_casing_calc.is_valid():
            casing = form_casing_calc.cleaned_data.get("casing")
            casing_color = form_casing_calc.cleaned_data.get("casing_color")
            length = form_casing_calc.cleaned_data.get("length")
            width = form_casing_calc.cleaned_data.get("width")
            count = form_casing_calc.cleaned_data.get("count")
            calc_casing(order_id=pk, casing=casing, width=width, length=length, casing_color=casing_color,
                        count=count)
            return redirect('order', pk=pk, form='casing_calc')

        form_slopes_of_metal_calc = SlopesOfMetalCalcForm(request.POST)
        if form_slopes_of_metal_calc.is_valid():
            slopes_of_metal = form_slopes_of_metal_calc.cleaned_data.get("slopes_of_metal")
            slopes_of_metal_color = form_slopes_of_metal_calc.cleaned_data.get("slopes_of_metal_color")
            length = form_slopes_of_metal_calc.cleaned_data.get("length")
            width = form_slopes_of_metal_calc.cleaned_data.get("width")
            count = form_slopes_of_metal_calc.cleaned_data.get("count")
            calc_slopes_of_metal(order_id=pk, slopes_of_metal=slopes_of_metal,
                                 slopes_of_metal_color=slopes_of_metal_color,
                                 width=width, length=length,
                                 count=count)
            return redirect('order', pk=pk, form='slopes_of_metal_calc')

        form_internal_slopes_calc = InternalSlopesCalcForm(request.POST)
        if form_internal_slopes_calc.is_valid():
            internal_slopes = form_internal_slopes_calc.cleaned_data.get("internal_slopes")
            internal_slopes_color = form_internal_slopes_calc.cleaned_data.get("internal_slopes_color")
            length = form_internal_slopes_calc.cleaned_data.get("length")
            width = form_internal_slopes_calc.cleaned_data.get("width")
            count = form_internal_slopes_calc.cleaned_data.get("count")
            calc_internal_slopes(order_id=pk, internal_slopes=internal_slopes,
                                 internal_slopes_color=internal_slopes_color,
                                 width=width, length=length,
                                 count=count)
            return redirect('order', pk=pk, form='internal_slopes_calc')

        form_mounting_materials_calc = MountingMaterialsCalcForm(request.POST)
        if form_mounting_materials_calc.is_valid():
            mounting_materials = form_mounting_materials_calc.cleaned_data.get("mounting_materials")
            count = form_mounting_materials_calc.cleaned_data.get("count")
            calc_mounting_materials(order_id=pk, mounting_materials=mounting_materials,
                                    count=count)
            return redirect('order', pk=pk, form='mounting_materials_calc')

        form_works_calc = WorksCalcForm(request.POST)
        if form_works_calc.is_valid():
            works = form_works_calc.cleaned_data.get("works")
            count = form_works_calc.cleaned_data.get("count")
            calc_works(order_id=pk, works=works,
                       count=count)
            return redirect('order', pk=pk, form='works_calc')
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = Order.objects.get(pk=pk)
            order.address = form_order.cleaned_data.get("address")
            order.name = form_order.cleaned_data.get("name")
            order.phone = form_order.cleaned_data.get("phone")
            order.date = form_order.cleaned_data.get("date")
            order.user = user
            order.save()
            return redirect('order', pk=pk, form='None')

    calc_order(order_id=pk)
    order = Order.objects.get(pk=pk)

    windowsill_calc = WindowsillCalc.objects.filter(order_id=pk).order_by('-id')
    low_tides_calc = LowTidesCalc.objects.filter(order_id=pk).order_by('-id')
    visors_calc = VisorsCalc.objects.filter(order_id=pk).order_by('-id')
    flashing_calc = FlashingCalc.objects.filter(order_id=pk).order_by('-id')
    casing_calc = CasingCalc.objects.filter(order_id=pk).order_by('-id')
    slopes_of_metal_calc = SlopesOfMetalCalc.objects.filter(order_id=pk).order_by('-id')
    internal_slopes_calc = InternalSlopesCalc.objects.filter(order_id=pk).order_by('-id')
    mounting_materials_calc = MountingMaterialsCalc.objects.filter(order_id=pk).order_by('-id')
    works_calc = WorksCalc.objects.filter(order_id=pk).order_by('-id')

    form_order = OrderForm(initial={
        'address': order.address,
        'name': order.name,
        'phone': order.phone,
        'date': order.date,
        'status': order.status,

    })
    form_windowsill_calc = WindowsillCalcForm(
        initial={'windowsill_count': 1, 'windowsill': 1, 'windowsill_color': 1, 'windowsill_plug': 1, })

    form_low_tides_calc = LowTidesCalcForm(
        initial={'low_tides_count': 1, 'low_tides': 1, 'low_tides_type': 1, 'low_tides_color': 1, 'low_tides_plug': 1})

    form_visors_calc = VisorsCalcForm(initial={'count': 1, 'visors_color': 1})

    form_flashing_calc = FlashingCalcForm(initial={'count': 1, 'flashing_color': 1})

    form_casing_calc = CasingCalcForm(initial={'count': 1, 'casing_color': 1})

    form_slopes_of_metal_calc = SlopesOfMetalCalcForm(initial={'count': 1, 'slopes_of_metal_color': 1})

    form_internal_slopes_calc = InternalSlopesCalcForm(initial={'count': 1, 'internal_slopes_color': 1})

    form_mounting_materials_calc = MountingMaterialsCalcForm(initial={'count': 1})

    form_works_calc = WorksCalcForm(initial={'count': 1})

    context = {
        'form': form,
        'order': order,

        'form_order': form_order,

        'form_windowsill_calc': form_windowsill_calc,
        'windowsill_calc': windowsill_calc,

        'form_low_tides_calc': form_low_tides_calc,
        'low_tides_calc': low_tides_calc,

        'form_visors_calc': form_visors_calc,
        'visors_calc': visors_calc,

        'form_flashing_calc': form_flashing_calc,
        'flashing_calc': flashing_calc,

        'form_casing_calc': form_casing_calc,
        'casing_calc': casing_calc,

        'form_slopes_of_metal_calc': form_slopes_of_metal_calc,
        'slopes_of_metal_calc': slopes_of_metal_calc,

        'form_internal_slopes_calc': form_internal_slopes_calc,
        'internal_slopes_calc': internal_slopes_calc,

        'form_mounting_materials_calc': form_mounting_materials_calc,
        'mounting_materials_calc': mounting_materials_calc,

        'form_works_calc': form_works_calc,
        'works_calc': works_calc,

    }
    return render(request, 'measurer_window/order_detail.html', context)


def home(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('accounts/login/')

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
            return redirect('order', pk=order.pk, form=None)

    orders = Order.objects.filter(user=user).order_by('-pk')
    form_order = OrderForm(initial={'phone': "+375"})
    context = {
        'form_order': form_order,
        'orders': orders,
    }
    return render(request, 'measurer_window/home.html', context)
