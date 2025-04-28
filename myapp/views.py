from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  # Import authenticate, login, and logout
from django.contrib.auth.models import User  # Import User model for registration
from .models import Product, Order

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})  # Render all products on index page

def about(request):
    return render(request, "about.html")

def booking(request):
    return render(request, "booking.html")

def contact(request):
    return render(request, "contact.html")

def menu(request):
    return render(request, "menu.html")

def team(request):
    return render(request, "team.html")

def service(request):
    return render(request, "service.html")

def testimonial(request):
    return render(request, "testimonial.html")

def home(request):
    return render(request, 'home.html')  # Render your home page template

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                # Automatically log the user in after registration
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)  # Logs the user in
                    messages.success(request, 'Registration successful! You are now logged in.')
                    return redirect('index')  # Redirect to home page
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')

def login_view(request):  # Make sure this function name is 'login_view'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

def logout_view(request):  
    logout(request)
    return redirect('index')

def OrderProduct(request, pk):  # View for handling product orders
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    if user.is_authenticated:
        order = Order.objects.create(user=user, product=product)
        order.save()
        messages.success(request, 'Order created successfully. Your order is on the way!')
        return redirect('index')
