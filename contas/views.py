from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Entregue').count()
    pending = orders.filter(status='Pendente').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}

    return render(request, 'contas/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'contas/products.html', {'products':products})

def customer(request):
    return render(request, 'contas/customer.html')
