# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import BuyerSignUpForm, SellerSignUpForm, BuyerLoginForm, SellerLoginForm

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
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active and user.is_buyer:
                login(request, user)
                return redirect('buyer_dashboard')
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
