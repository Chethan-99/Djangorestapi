from django.db.models import fields
from django.shortcuts import render
from rest_framework import generics

from djangorestAPIapp.models import Book, Category, Product, Cart, User
from .serializers import CategorySerializer, BookSerializer,ProductSerializer, CartSerializer, UserSerializer

from rest_framework import permissions

# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListBook(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer 


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListProduct(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   