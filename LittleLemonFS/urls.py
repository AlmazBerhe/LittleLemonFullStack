from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("menu", views.menu, name="menu"),
    path("menu-item/<int:pk>", views.display_menu_item, name="menu_item"),
    path("book", views.BookingView.as_view(), name="book"),
    path("bookings", views.BookingsView.as_view(), name="bookings"),
    path("reservations", views.ReservationsView.as_view(), name="reservations"),
]