from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from cartmanager.models import Cart, Entry
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cartmanager.serializers import CartSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import  permission_classes

from customermanager.models import Customer
from productmanager.models import Product


# Create your views here.

@api_view(["GET","PUT","DELETE"])
@permission_classes([AllowAny])
def show_cart_by_id(request,id):
    cart = get_object_or_404(Cart, id=id)
    if request.method == "GET":
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        cart.delete()
        return Response(data="msg: the resource has been deleted",status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        cart_serializer = CartSerializer(cart,data=request.data)
        if cart_serializer.is_valid():
            cart_serializer.update(cart,request.data)
            return Response(cart_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","POST"])
@permission_classes([AllowAny])
def show_all_carts(request):
    if request.method == "GET":
        carts = get_list_or_404(Cart)
        serialized_carts = CartSerializer(carts, many=True)
        return Response(serialized_carts.data)
    elif request.method == "POST":
        cart_serializer = CartSerializer(data=request.data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(cart_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
@permission_classes([IsAuthenticated]) # nur eingeloggte user

def add_to_cart(request):
    customer = Customer.objects.get(user=request.user) #das anstatt get list or 404
    try:
        cart = Cart.objects.get(customer=customer)
    except Cart.DoesNotExist:
        cart = Cart(customer=customer)
        cart.save()

    product_id = request.data.get('product')
    quantity = request.data.get('quantity')

    if all([product_id,quantity]): #prüft ob alle iterierbaren Daten nicht null sind, wenn nicht null dann springen wir ins if
        product = get_object_or_404(Product, id=product_id)
        cart_entry = Entry(product_id = product.id,quantity = quantity, product_name= product.name,
                           unit_net_price = product.price_netto, unit_gross_price = product.price_brutto, net_sum = quantity*float(product.price_netto),
                           gross_sum= quantity*float(product.price_brutto), cart=cart) # durch das float ändern wir price brutto in ein float
        cart_entry.save()
        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("Product or quanity are required", status=status.HTTP_400_BAD_REQUEST)

    # 1 Versuche Cart von Customer zu holen
    # wenn erfolgreich : Erstelle Cart Entry und füge es zum bestehenden cart hinzu und speicher es
    #wenn nicht erfolgreich: erstelle einen cart, cart speichern, erstelle cart entry, carty entry speichern



