from rest_framework import serializers
from .models import Booking

class BookingsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = "__all__"
        
class SingleBookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = "__all__"