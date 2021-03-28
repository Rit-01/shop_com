from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from shop.models.customer import Customer
from django.views import View

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                #save customer object without jason request
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                #end code for save
                return redirect('shop')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid'
            print(email, password)

        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')