from rest_framework import serializers 
from .models import Estate,Booking


class Estateserializer(serializers.ModelSerializer):
    class Meta:
        model= Estate
        fields= "__all__"

class Bookingserializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields= "__all__"