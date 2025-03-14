from uuid import uuid4
from django.db.models import (
    Model,
    CharField,
    TextChoices,
    UUIDField,
    ForeignKey,
    IntegerField,
    CASCADE,
    FloatField,
)

# In this file all database models for Products API is defined.
# This functions as a schema for the tables of the database where constraints etc. are defined


class Manufacturer(Model):
    class ManufacturerChoices(TextChoices):
        AMERICAN_HOME_FOOD_PRODUCTS = "A"
        GENERAL_MILLS = "G"
        KELLOGGS = "K"
        NABISCO = "N"
        POST = "P"
        QUAKER_OATS = "Q"
        RALSTON_PURINA = "R"

    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    code = CharField(
        max_length=1, choices=ManufacturerChoices.choices, unique=True, null=False
    )

    def __str__(self):
        return self.code


class ThermalType(Model):
    class ThermalChoices(TextChoices):
        COLD = "C"
        HOT = "H"

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    code = CharField(
        max_length=1,
        choices=ThermalChoices.choices,
        default=ThermalChoices.COLD,
        unique=True,
        null=False,
    )

    def __str__(self):
        self.ThermalChoices.choices
        return self.code


class Product(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=255, unique=True, null=False)
    mfr = ForeignKey(Manufacturer, on_delete=CASCADE, null=False, editable=True)
    thermal_type = ForeignKey(ThermalType, on_delete=CASCADE, null=False, editable=True)
    calories = IntegerField(null=False)
    protein = IntegerField(null=False)
    fat = IntegerField(null=False)
    sodium = IntegerField(null=False)
    fiber = FloatField(null=False)
    carbo = FloatField(null=False)
    sugars = IntegerField(null=False)
    potass = IntegerField(null=False)
    vitamins = IntegerField(null=False)
    shelf = IntegerField(null=False)
    weight = FloatField(null=False)
    cups = FloatField(null=False)
    rating = CharField(max_length=255, null=False)
