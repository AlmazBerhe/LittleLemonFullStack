from django.shortcuts import render, HttpResponse
from django.core import serializers
from .forms import BookingForm
from .models import Booking, Menu
from rest_framework import generics, status
from datetime import datetime


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', main_data)


class BookingView(generics.RetrieveUpdateDestroyAPIView):
    
    def get(self, request):
        return render(request, 'book.html', {'form': BookingForm})


class BookingsView(generics.ListAPIView):
    
    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        bookings = Booking.objects.all()
        booking_json = serializers.serialize('json', bookings)
        context = {'bookings': booking_json}
        
        return render(request, 'bookings.html', context, status=status.HTTP_200_OK)
    
    # def post(self, request):
        