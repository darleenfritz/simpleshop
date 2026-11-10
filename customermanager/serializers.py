from pickle import FALSE
from rest_framework import serializers
from addressmanager.serializers import AddressSerializer
from customermanager.models import Customer
from django.contrib.auth.models import User

class CustomerSerializer(serializers.Serializer):
    salutation = serializers.CharField(max_length=5)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    birthday = serializers.DateField()
    addresses = AddressSerializer(many =True, read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=128)

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        birthday = validated_data.get('birthday')
        password = validated_data.get('password')
        salutation = validated_data.get('salutation')
        email = validated_data.get('email')
        user = User.objects.create_user(first_name=first_name, last_name=last_name,username = email, password=password, email = email)
        customer= Customer.objects.create(user=user, salutation=salutation,birthday=birthday)
        return customer


    def update(self, instance, validated_data):
        instance.salutation = validated_data.get('salutation')
        instance.user.first_name = validated_data.get('first_name')
        instance.user.last_name = validated_data.get('last_name')
        instance.birthday = validated_data.get('birthday')
        instance.save()
        return instance

