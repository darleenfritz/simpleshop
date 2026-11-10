from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from addressmanager.models import Address
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from addressmanager.serializers import AddressSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import  permission_classes

# Create your views here.

@api_view(["GET", "PUT", "DELETE"])
def show_address_by_id(request,id):
    address = get_object_or_404(Address, id=id)
    if request.user == address.customer.user or request.user.is_staff:
        if request.method == "GET":
            serializer = AddressSerializer(address)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            address.delete()
            return Response(data="msg: the resource has been deleted",status=status.HTTP_204_NO_CONTENT)
        elif request.method == "PUT":
            address_serializer = AddressSerializer(address,data=request.data)
            if address_serializer.is_valid():
                address_serializer.update(address,request.data)
                return Response(address_serializer.data)
            else:
                return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        raise PermissionDenied


@api_view(["GET","POST"])
@permission_classes([AllowAny])
def show_all_addresses(request):
    if request.method == "GET":
        if request.user.is_staff:
            addresses = get_list_or_404(Address)
            serialized_addresses = AddressSerializer(addresses, many=True)
            return Response(serialized_addresses.data)
        else:
            raise PermissionDenied
    elif request.method == "POST":
        address_serializer = AddressSerializer(data=request.data)
        if address_serializer.is_valid():
            address_serializer.save()
            return Response(address_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


