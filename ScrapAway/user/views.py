# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import BuyerSignUpForm, SellerSignUpForm, BuyerLoginForm, SellerLoginForm
from .models import PickupRequest


def landing(request):
    # Your view logic here
    return render(request, 'index.html')  # Assuming 'landing.html' is your landing page template


def buyer_signup(request):
    if request.method == 'POST':
        form = BuyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_buyer = True
            user.save()
            # You may add additional logic here, e.g., redirect to login page with a success message
            return redirect('buyer_login')
    else:
        form = BuyerSignUpForm()
        print("form not valid")
    return render(request, 'buyer_signup.html', {'form': form})

def seller_signup(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_seller = True
            user.save()
            # You may add additional logic here, e.g., redirect to login page with a success message
            return redirect('seller_login')
    else:
        form = SellerSignUpForm()
    return render(request, 'seller_signup.html', {'form': form})

def buyer_login(request):
    if request.method == 'POST':
        form = BuyerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.is_buyer:
                        login(request, user)
                        print("Buyer logged in successfully")
                        return redirect('buyer_dashboard')
                    else:
                        print("User is not a buyer")
                else:
                    print("User account is not active")
            else:
                print("Invalid username or password")
        else:
            print("Form errors:", form.errors)
            print("Form cleaned data:", form.cleaned_data)
    else:
        form = BuyerLoginForm()
    return render(request, 'buyer_login.html', {'form': form})


def seller_login(request):
    if request.method == 'POST':
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active and user.is_seller:
                login(request, user)
                return redirect('seller_dashboard')
    else:
        form = SellerLoginForm()
    return render(request, 'seller_login.html', {'form': form})

def buyer_dashboard(request):
    print("Buyer dashboard accessed")
    pickup_request = PickupRequest.objects.all()
    context = {
        'requests': pickup_request
    }
    return render(request, 'buyer_dashboard.html', context )




