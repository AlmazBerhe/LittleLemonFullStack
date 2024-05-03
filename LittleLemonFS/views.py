from django.shortcuts import render, HttpResponse
from django.core import serializers
from .forms import BookingForm
from .models import Booking, Menu
from rest_framework import generics, status
from datetime import datetime
from .serializers import BookingsSerializer, SingleBookingSerializer


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})


class BookingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SingleBookingSerializer
    
    
    def get(self, request):
        return render(request, 'book.html', {'form': BookingForm})
    
    def post(self, request):
        first_name = request.data.get("first_name")
        reservation_date = request.data.get("reservation_date")
        reservation_slot = request.data.get("reservation_slot")
        
        booking = Booking(
            first_name= first_name, 
            reservation_date=reservation_date, 
            reservation_slot=reservation_slot
            )
        booking.save()
        
        return render(request, 'book.html', {'form': BookingForm})


class BookingsView(generics.ListAPIView):
    serializer_class = BookingsSerializer
    
    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        bookings = Booking.objects.all()
        
        if not bookings:
            return render(request, 'bookings.html', {'message': ""}, status=status.HTTP_200_OK)
        
        booking_json = serializers.serialize('json', bookings)
        context = {'bookings': booking_json}
        
        return render(request, 'bookings.html', context, status=status.HTTP_200_OK)
    
    