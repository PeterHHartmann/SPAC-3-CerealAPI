from django.shortcuts import render
from rest_framework import permissions, viewsets

from cereal_api.models import Cereal, Manufacturer, ThermalType
from cereal_api.serializers import CerealSerializer, ManufacturerSerializer

# Create your views here.


class CerealViewSet(viewsets.ModelViewSet):
    queryset = Cereal.objects.all().order_by("name")
    serializer_class = CerealSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by("code")
    serializer_class = ManufacturerSerializer


class ThermalTypeViewSet(viewsets.ModelViewSet):
    queryset = ThermalType.objects.all().order_by("code")
    serializer_class = ManufacturerSerializer
