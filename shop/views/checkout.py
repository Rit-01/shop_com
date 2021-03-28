from django.shortcuts import render, redirect
from django.views import View
from shop.models.product import Product
from shop.models.orders import Order
from shop.models.customer import Customer



class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.get_product_by_id(list(cart.keys()))
        print(address, phone, state, zipcode, customer, cart, product)


        for product in product:
            print(cart.get(str(product.id)))
            order = Order(customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          zipcode = zipcode,
                          state = state,
                          quantity = cart.get(str(product.id)))

            order.save()


            # after checkout cart clear--------------
            request.session['cart'] = {}

        return redirect('cart')
      