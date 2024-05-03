from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("menu", views.menu, name="menu"),
    path("book", views.BookingView.as_view(), name="book"),
    path("bookings", views.BookingsView.as_view(), name="bookings"),
]