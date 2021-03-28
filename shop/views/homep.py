from django.shortcuts import render, redirect
from shop.models.product import Product
from shop.models.category import Category
from django.views import View


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' ,request.session['cart'])
        return redirect('shop')
        

    def get(self, request):
         # use for category showes and dainamicay work
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
       # print('you are : ' ,request.session.get('email'))
        return render(request, 'index.html', data)

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')