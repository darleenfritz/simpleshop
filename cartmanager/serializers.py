from rest_framework import serializers

from cartmanager.models import Cart, Entry


class Cart_EntrySerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=100)
    unit_net_price = serializers.FloatField()
    unit_gross_price = serializers.FloatField()
    quantity = serializers.IntegerField()
    net_sum = serializers.FloatField()
    gross_sum = serializers.FloatField()


class CartSerializer(serializers.Serializer):
    cart_netto = serializers.FloatField()
    taxes = serializers.FloatField()
    cart_brutto = serializers.FloatField()
    entries = Cart_EntrySerializer(many=True, required=False)
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cart_netto= validated_data.get('cart_netto')
        instance.taxes = validated_data.get('taxes')
        instance.cart_brutto = validated_data.get('cart_brutto')
        instance.save()
        return instance



