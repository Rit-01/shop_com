from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.customer import Customer
from django.views import View


# when request from user then it can be run and it is code be write only for register user
# if user is not register

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        # customer object

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )

        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)

            # password hashing
            customer.password = make_password(customer.password)

            customer.register()
            return render(request, 'login.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First name must be 4 Char long !'
        elif not customer.last_name:
            error_message = "last name Required !!"
        elif len(customer.last_name) < 3:
            error_message = 'last name must be 3 Char long !'
        elif not customer.phone:
            error_message = 'Phone number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone number must be 10 degit'
        elif len(customer.password) < 6:
            error_message = ' Possword must be 6 char'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char'
        elif customer.isExists():
            error_message = 'Email address already register....'

        return error_message
