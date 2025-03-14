from rest_framework import serializers
from cereal_api.models import Cereal, Manufacturer, ThermalType


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "url", "code"]


class ThermalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThermalType
        fields = ["id", "url", "code"]


class CerealSerializer(serializers.HyperlinkedModelSerializer):

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
        model = Cereal
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
