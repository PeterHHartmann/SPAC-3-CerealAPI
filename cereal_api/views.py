from django.shortcuts import render
from rest_framework import permissions, viewsets

from cereal_api.models import Cereal, Manufacturer, ThermalType
from cereal_api.serializers import CerealSerializer, ManufacturerSerializer, ThermalTypeSerializer

# Create your views here.


class CerealViewSet(viewsets.ModelViewSet):
    queryset = Cereal.objects.all().order_by("name")
    serializer_class = CerealSerializer

    def create(self, request, *args, **kwargs):
        # data = request.data
        # print(data)
        # thermal_c = request.data.get('thermal_type.code')
        # print(f"thermal_c: {thermal_c}")
        # thermal_code = ThermalType.objects.get(code=request.data.get('thermal_type.code'))

        # print(f"thermal_code: {thermal_code}")
        # cereal = Cereal(request.data)
        # print(cereal)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print('UPDATE RAN')
        return super().update(request, *args, **kwargs)




class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by("code")
    serializer_class = ManufacturerSerializer


class ThermalTypeViewSet(viewsets.ModelViewSet):
    queryset = ThermalType.objects.all().order_by("code")
    serializer_class = ThermalTypeSerializer
