from rest_framework import serializers
from cereal_api.models import Cereal, Manufacturer, ThermalType


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'url', 'code']


class ThermalTypeSerializer(serializers.ModelSerializer):
    # def validate(self, attrs):
    #     print('we got here')
    #     return True
        # return super().validate(attrs)
    class Meta:
        model = ThermalType
        fields = ["id", "url", "code"]

    def is_valid(self, *, raise_exception=False):
        print('got here')
        return super().is_valid(raise_exception=raise_exception)
    

class CerealSerializer(serializers.HyperlinkedModelSerializer):

    # mfr = ManufacturerSerializer()

    # mfr = serializers.ModelSerializer()

    mfr = serializers.SlugRelatedField(
        queryset=Manufacturer.objects.all(),
        many=False, 
        read_only=False,
        slug_field='code',
    )

    thermal_type = serializers.SlugRelatedField(
        queryset=ThermalType.objects.all(),
        many=False,
        read_only=False,
        slug_field='code'
    )

    # thermal_type = ThermalTypeSerializer(many=False)

    class Meta:
        model = Cereal
        fields = [
            "id",
            "url",
            "name",
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
            "mfr",
            "thermal_type"
        ]
        depth = 1

    # def is_valid(self, *, raise_exception=False):
    #     try:
    #         thermal = self.data.get("thermal_type")
    #         print('got here')
    #         # print(dir(self))
    #         print()
    #         print(thermal)
    #     except Exception as e:
    #         print(e)
    #     return super().is_valid(raise_exception=raise_exception)

    # def create(self, validated_data):
    #     print('got here - create')
    #     thermaltype_data = validated_data.pop['thermal_type.code']
    #     cereal = Cereal.objects.create(**validated_data)
    #     return cereal
    # def create(self, validated_data):
    #     mfr_data = validated_data.pop('mfr')
    #     print(mfr_data)
    #     return super().create(validated_data)
