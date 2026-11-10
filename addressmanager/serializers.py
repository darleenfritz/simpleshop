from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.Serializer):
    salutation = serializers.CharField(max_length=5)
    firstname = serializers.CharField(max_length=20)
    lastname = serializers.CharField(max_length=20)
    street = serializers.CharField(max_length=100)
    housenumber = serializers.IntegerField()
    zip = serializers.IntegerField()
    city = serializers.CharField(max_length=20)
    delivery_zone = serializers.SerializerMethodField(method_name='get_delivery_zone') # wird ignoriert und selbst berechnet muss man nicht mitgeben
    id = serializers.IntegerField(required=False)
    customer_id = serializers.IntegerField(required=False)



    def get_delivery_zone(self, address:Address):
        if str(address.zip).startswith('7') or str(address.zip).startswith('8'):
            return 'SOUTH_GERMANY'
        elif str(address.zip).startswith('0') or str(address.zip).startswith('3') or str(address.zip).startswith('4') or str(address.zip).startswith('5') or str(address.zip).startswith('6'):
            return 'CENTRAL_GERMANY'
        elif str(address.zip).startswith('2') or str(address.zip).startswith('1'):
            return 'NORTH_GERMANY'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.salutation = validated_data.get('salutation')
        instance.firstname = validated_data.get('firstname')
        instance.lastname = validated_data.get('lastname')
        instance.street = validated_data.get('street')
        instance.housenumber = validated_data.get('housenumber')
        instance.zip = validated_data.get('zip')
        instance.city = validated_data.get('city')
        instance.delivery_zone = validated_data.get('delivery_zone')
        instance.save()
        return instance

