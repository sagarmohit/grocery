from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Products, Cart , CategorySelected

    # Create your views here.
def index(request):

    return render(request , 'index.html',)

def loginpage(request):
    return render(request , 'login.html')

def register(request):
    return render(request , 'registration.html')

def home(request):

    return render(request , 'index.html')

def addtodb(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            if User.objects.filter(username=name).exists():
                msg='Username already exist'
                return render(request, 'registration.html', {'msg': msg})
            elif User.objects.filter(email=email).exists():
                msg='Email already exist'
                return render(request, 'registration.html', {'msg': msg})

            else:
                user = User.objects.create_user(username=name, email=email, password=pass1)

                return redirect('login' )
        else :
            msg = 'password mismatch'
            return render(request, 'registration.html', {'msg':msg})
    else:
        print(' enter correct data')


def userlogin(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        global user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/')
        else:
            msg = 'INVALID USERNAME OR PASSWORD'
            return render(request, 'login.html', {'msg':msg})

    else:
        return render(request, 'login.html')


def userlogout(request):
    logout(request)
    return render(request, 'index.html')

def selectedcategory(request):
    try:
        if request.method == 'GET':

            category1 = request.GET['category']
            request.session['categoryselected']= category1
            product = Products.objects.filter(category=category1)
            return render(request, 'products.html' , { 'product':product})
    except NameError or AttributeError:
        logout(request)
        msg = 'Login again'
        return render(request, 'login.html', {'msg2': msg})

def addtocart(request):

    try:
        if request.method == 'GET':

            item = request.GET['item']
            productselected = Products.objects.get(productcode=item)
            username = user.username
            productcode = productselected.productcode
            category = productselected.category
            price = productselected.offerprice
            name = productselected.name
            image = productselected.image.url
            amount = productselected.amount

            Cart.objects.create(username=username, productcode=productcode, category=category, price=price, name=name,
                                image=image, amount=amount)
            msg = 'added to cart'

            category2= request.session['categoryselected']
            product = Products.objects.filter(category=category2)
            return render(request, 'products.html', {'product': product, 'msg3':msg})
        else:

            return render(request, 'index.html')
    except NameError:
        logout(request)
        msg = 'Login again'
        return render(request, 'login.html', {'msg2' : msg})

def cart(request):

    try:
        username= user.username
        myproducts = Cart.objects.filter(username=username)
        totalprice = 0
        for product in myproducts:
            totalprice += product.price
        return render(request, 'cart.html', {'myproducts':myproducts, 'totalprice':totalprice})
    except NameError:
        logout(request)
        msg = 'Login again'
        return render(request, 'login.html', {'msg2' : msg})

def deleteitem(request):
    if request.method == 'GET':
        item = request.GET['deleteitem']
        Cart.objects.filter(productcode=item).delete()
        return redirect('cart')