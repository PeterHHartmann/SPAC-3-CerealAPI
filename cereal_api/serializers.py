from rest_framework import serializers
from cereal_api.models import Cereal, Manufacturer, ThermalType


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "code"]


class ThermalTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThermalType
        fields = ["id", "code"]


class CerealSerializer(serializers.HyperlinkedModelSerializer):

    mfr = ManufacturerSerializer(
        many=False,
        read_only=True,
    )

    thermal_type = ThermalTypeSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        model = Cereal
        fields = [
            "id",
            "name",
            "mfr",
            "thermal_type",
            "calories",
            "protein",
            "fat",
            "sodium",
            "fiber",
            "carbo",
            "potass",
            "vitamins",
            "shelf",
            "weight",
            "cups",
            "rating",
        ]
