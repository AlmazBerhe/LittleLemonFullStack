from django.shortcuts import render, HttpResponse
from django.core import serializers
from .forms import BookingForm
from .models import Booking, Menu
from rest_framework import generics, status
from datetime import datetime
from .serializers import BookingsSerializer, SingleBookingSerializer
from django.http import JsonResponse


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
        date = request.GET.get('date',datetime.today().date())
        bookings = []
        if date:
            bookings = Booking.objects.all().filter(reservation_date=date)
            
        return render(request, 'book.html', {'form': BookingForm, 'bookings': bookings})
    
    def post(self, request):
        first_name = request.data.get("first_name")
        reservation_date = request.data.get("reservation_date")
        reservation_slot = request.data.get("reservation_slot")
        
        exist = Booking.objects.filter(reservation_date=reservation_date).filter(reservation_slot=reservation_slot)
        
        if not exist:
        
            booking = Booking(
                first_name= first_name, 
                reservation_date=reservation_date, 
                reservation_slot=reservation_slot
                )
            booking.save()
                        
            return render(request, 'book.html', {'form': BookingForm, 'reservation_date': reservation_date})
        
        return HttpResponse("{'error': 1}", content_type='application/json')
        
class BookingsView(generics.ListAPIView):
    serializer_class = BookingsSerializer
    
    def get(self, request):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.all().filter(reservation_date=date)
        else:
            bookings = Booking.objects.all()
            
        booking_data = list(bookings.values())
        
        return JsonResponse(booking_data, safe=False)

class ReservationsView(generics.ListAPIView):
    serializer_class = BookingsSerializer
    
    def get(self, request):
        
        bookings = Booking.objects.all()
            
        bookings_data = serializers.serialize('json', bookings)
            
        return render(request, 'bookings.html', {'bookings': bookings_data})
      
    
    