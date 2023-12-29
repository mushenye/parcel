from django import forms


from django.forms import ModelForm

from sending.models import Parcel, Person


class PersonForm(ModelForm):

    class Meta:
        model= Person
        fields= '__all__'


class ParcelForm(ModelForm):

    class Meta:
        model= Parcel
        fields= '__all__'
        exclude = ('is_recieved','is_shipped',)
