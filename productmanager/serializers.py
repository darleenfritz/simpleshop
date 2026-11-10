from pickle import FALSE
from rest_framework import serializers
from productmanager.models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    product_number = serializers.IntegerField()
    price_brutto = serializers.DecimalField(max_digits=5, decimal_places=2)
    price_netto = serializers.DecimalField(max_digits=5, decimal_places=2)
    id = serializers.IntegerField(required=False)


    def create(self, validated_data):
        return Product.objects.create(**validated_data)


    def update(self, instance:Product, validated_data):
        instance.name = validated_data.get('name')
        instance.product_number = validated_data.get('product_number')
        instance.price_brutto = validated_data.get('price_brutto')
        instance.price_netto = validated_data.get('price_netto')
        instance.save()
        return instance


