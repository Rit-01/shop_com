from django.shortcuts import render, redirect
from django.views import View
from shop.models.product import Product
from shop.models.orders import Order
from shop.models.customer import Customer
from shop.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator



class OrderView(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html',{'orders': orders})
