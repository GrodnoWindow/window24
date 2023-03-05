from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import *


# Create your views here.

class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"


def home(request):
    username = User.objects.get(username=request.user.username)
    orders = Order.objects.filter(user=username)
    context = {
        'test': 'test',
        'orders': orders,
    }
    return render(request, 'measurer_window/home.html', context)


def order(request,pk):
    # username = User.objects.get(username=request.user.username)
    order = Order.objects.get(pk=pk)
    # print(pk)
    context = {
        'order': order,
    }
    return render(request, 'measurer_window/order_detail.html', context)
