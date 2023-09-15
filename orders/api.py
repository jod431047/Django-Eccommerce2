from rest_framework import generics
from .models import Cart , Order , OrderDetail , CartDetail
from . serializers import CartDetailSerializer ,CartSerializer
from django.contrib.auth.models import User