from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer
import random

# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        queryset = Product.objects.all()
        # list of products needs to return an array
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    # /api/products
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        # send valid data to serializer, if not, raise an exception
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_created", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # /api/products/<str:id>
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        # instance=product -> product that we already have
        # data=request.data -> data of product we want to update
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_updated", serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:id>
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        # send pk instead of object
        publish("product_deleted", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    # define get function with request in parameter, but we don't use it so use _ instead
    def get(self, _):
        users = User.objects.all()
        # get random user:
        user = random.choice(users)
        # return the random user:
        return Response({"id": user.id})
