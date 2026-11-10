from email.header import Header
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from customermanager.models import Customer
from customermanager.serializers import CustomerSerializer
from productmanager.models import Product


# Create your views here.
@api_view()
def show_all_customers(request):
    firstname = request.query_params.get('firstname')
    lastname = request.query_params.get('lastname')
    if firstname is not None and lastname is not None:
        customers = get_list_or_404(Customer, firstname__contains=firstname, lastname__contains=lastname)
    elif firstname is not None:
        customers=get_list_or_404(Customer, firstname__contains=firstname)
    elif lastname is not None:
        customers=get_list_or_404(Customer, lastname__contains=lastname)
    else:
        customers=get_list_or_404(Customer)

    serialized_customers = CustomerSerializer(customers, many =True)
    return Response(serialized_customers.data)

@api_view(["GET","PUT","DELETE"])
def show_customer_by_id(request,id):
    customer = get_object_or_404(Customer, id=id)
    if request.user == customer.user:
        if request.method == "GET":
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "PUT":
            serializer = CustomerSerializer(customer,data=request.data)
            if serializer.is_valid():
                serializer.update(customer, request.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            customer.delete()
            return Response(data="msg: The resource has been deleted", status=status.HTTP_204_NO_CONTENT)
    else:
        raise PermissionDenied

@api_view(["GET","POST"])
@permission_classes([AllowAny])
def show_customers(request):
    if request.method == "GET":
        if request.user.is_staff:
            customers = get_list_or_404(Customer)
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied
    elif request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show_first_customer(request):
    customer = Customer.objects.first()
    return HttpResponse(f"Vorname: {customer.firstname}, Geburtsdatum: {customer.birthday}")

def write_customer(request):
    customer = Customer(salutation = "Frau",firstname="Erika",lastname="Musterfrau",password = "test3",birthday = "2024-01-06", email = "erika@example.com")
    customer.save()
    customer = Customer.objects.last()
    return HttpResponse(f"Vorname: {customer.firstname}, Geburtsdatum: {customer.birthday}")



