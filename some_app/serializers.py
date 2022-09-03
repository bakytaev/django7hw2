from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if any(x in "!@#$%^&*" for x in value):
            raise serializers.ValidationError('Название категорий не может содержать символы !@#$%^&*')
        return value

    def validate(self, data):
        qr = f"{data['category_id']}C{data['price']}P{data['id']}I"
        if data['QR'] != qr:
            raise serializers.ValidationError("Неверный QR")
        return data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
