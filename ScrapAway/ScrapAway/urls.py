"""
URL configuration for ScrapAway project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('/signup', views.signup, name='signup'),
    path('/about', views.about, name='about'),
    path('buyer/login/', views.buyer_login, name='buyer_login'),
    path('seller/login/', views.seller_login, name='seller_login'),
    path('buyer/signup/', views.buyer_signup, name='buyer_signup'),  
    path('seller/signup/', views.seller_signup, name='seller_signup'),  
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('pickup/<int:id>', views.request_details, name='pickup_details'),
    path('pickup/<int:id>/accept', views.accept_request, name='accept_request'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),  

    #path('seller/sellerstatus/', views.seller_status, name='sell_status'),  



]\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

