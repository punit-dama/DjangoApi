from django.urls import path
from .views import OrdersView, StatusView
from django.conf import settings

urlpatterns = [
    path('orders/<int:id>/', OrdersView.as_view()),
    path('orders/', OrdersView.as_view()),
    path('status/<int:id>/', StatusView.as_view()),
]