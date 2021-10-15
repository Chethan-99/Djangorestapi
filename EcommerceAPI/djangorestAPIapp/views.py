from django.db.models import fields
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
import uuid

from djangorestAPIapp.models import Book, Category, Product, Cart, User
from .serializers import CategorySerializer, BookSerializer,ProductSerializer, CartSerializer, RegistrationSerializer, UserSerializer

from rest_framework import permissions

# Create your views here.

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save() or

        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId" : str(uuid.uuid4()),
                "Message": "User created Successfully",
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
    permission_class = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCart(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   