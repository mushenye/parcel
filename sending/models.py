import uuid
from django.db import models
from . choices import OFFICES


# Create your models here.
class Person (models.Model):
    name= models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    id_number=models.IntegerField()


class Parcel (models.Model):
    parcel_id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    created=models.DateTimeField(auto_now_add=True)
    sender= models.ForeignKey(Person, on_delete=models.CASCADE)
    reciever= models.OneToOneField(Person, on_delete=models.CASCADE, related_name= "reciever")
    origin = models.CharField(choices=OFFICES, max_length=100 )
    destination = models.CharField(choices=OFFICES, max_length=100 )
    description=models.TextField(max_length=200)
    is_shipped =models.BooleanField(default=False)
    is_recieved =models.BooleanField(default=False)


class Price (models.Model):
    parcel=models.ForeignKey(Parcel, on_delete=models.CASCADE)
    weight=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2, default=250)

class Shipping (models.Model):
    parcel=models.ForeignKey(Parcel, on_delete=models.CASCADE)
    vehicle_number=models.CharField(max_length=100)
    is_delivered =models.BooleanField(default=False) 

class Storage(models.Model):    
    store = models.CharField(choices=OFFICES, max_length=100 )
    storage_number=models.IntegerField(default=1)
    date=models.DateTimeField(auto_now_add=True)
    parcel=models.ForeignKey(Parcel, on_delete=models.CASCADE)

class Collect (models.Model):
    date_collected=models.DateTimeField(auto_now_add=True)
    parcel=models.ForeignKey(Parcel, on_delete=models.CASCADE)
    storage=models.ForeignKey(Storage, on_delete=models.CASCADE)
    person=models.ForeignKey(Person, on_delete=models.CASCADE)



