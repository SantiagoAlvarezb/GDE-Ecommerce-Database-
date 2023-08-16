from django.urls import path
from .views import *

# defining a URL pattern

urlpatterns = [
    path("process_order/", process_order, name="process_order"),
]
