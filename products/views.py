from rest_framework import viewsets

from products.models import Product, Manufacturer, ThermalType
from products.serializers import (
    ProductReadSerializer,
    ManufacturerSerializer,
    ProductWriteSerializer,
    ThermalTypeSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Viewset responsible for rendering views for all Product related data i.e. /products/ and /products/{pk}
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("name")
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = [
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

    def get_serializer_class(self):
        if self.request.method in ["POST"] or self.request.method in ["DELETE"]:
            return ProductWriteSerializer
        return ProductReadSerializer


# Viewset responsible for rendering views for all Manufacturer related data i.e. /manufacturers/ and /manufacturers/{pk}
class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by("code")
    serializer_class = ManufacturerSerializer


# Viewset responsible for rendering for all Manufacturer related data i.e. /thermaltypes/ and /thermaltypes/{pk}
class ThermalTypeViewSet(viewsets.ModelViewSet):
    queryset = ThermalType.objects.all().order_by("code")
    serializer_class = ThermalTypeSerializer
