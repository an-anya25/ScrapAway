from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    

    # class Meta:
    #     verbose_name = 'Custom User'
    #     verbose_name_plural = 'Custom Users'

# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)

# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)


STATUS_CHOICES = [
    ('PENDING', "Pending"),
    ('CONFIRMED', "Confirmed"),
    ('PICKED_UP', "Picked up"),
    ]

class PickupRequest(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    item_desc = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')





# Define related names for groups and user_permissions
# User._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
# User._meta.get_field('user_permissions').remote_field.related_name = 'customuser_permissions'
