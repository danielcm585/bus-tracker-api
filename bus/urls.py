from django.urls import path

from bus.views import *


urlpatterns = [
    path('hello/', hello),
]
