from django.contrib import admin
from django.db.models import Exists, OuterRef
from .models import User, PickupRequest

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_buyer', 'is_seller')

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.prefetch_related('buyer', 'seller')
    #     queryset = queryset.annotate(buyer_exists=Exists(Buyer.objects.filter(user_id=OuterRef('pk'))))
    #     queryset = queryset.annotate(seller_exists=Exists(Seller.objects.filter(user_id=OuterRef('pk'))))
    #     return queryset



class RequestAdmin(admin.ModelAdmin):
    list_display = ('seller','item')



admin.site.register(User, UserAdmin)
admin.site.register(PickupRequest, RequestAdmin)