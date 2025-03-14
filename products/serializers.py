from rest_framework import serializers
from products.models import Product, Manufacturer, ThermalType


# Serializer class for all Manufacturer requests
class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "url", "code"]


# Serializer class for all ThermalType requests
class ThermalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThermalType
        fields = ["id", "url", "code"]


# Serializer class for Product GET requests
class ProductReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "url",
            "name",
            "mfr",
            "thermal_type",
            "calories",
            "protein",
            "fat",
            "sodium",
            "fiber",
            "carbo",
            "sugars",
            "potass",
            "vitamins",
            "shelf",
            "weight",
            "cups",
            "rating",
        ]
        depth = 1


# Serializer class for Product POST/PUT/DELETE requests
class ProductWriteSerializer(serializers.HyperlinkedModelSerializer):

    mfr = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=False,
        view_name="manufacturer-detail",
        queryset=Manufacturer.objects.all(),
    )

    thermal_type = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=False,
        view_name="thermaltype-detail",
        queryset=ThermalType.objects.all(),
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "url",
            "name",
            "mfr",
            "thermal_type",
            "calories",
            "protein",
            "fat",
            "sodium",
            "fiber",
            "carbo",
            "sugars",
            "potass",
            "vitamins",
            "shelf",
            "weight",
            "cups",
            "rating",
        ]
