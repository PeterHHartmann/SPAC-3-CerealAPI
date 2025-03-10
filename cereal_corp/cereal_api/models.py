
from uuid import uuid4
from django.db.models import Model, CharField, TextChoices, IntegerChoices, UUIDField, ForeignKey, OneToOneField, CASCADE, PositiveIntegerField, FloatField
from django.core.validators import MaxValueValidator, MinValueValidator

class Manufacturer(Model):
    class ManufacturerChoices(TextChoices):
        AMERICAN_HOME_FOOD_PRODUCTS = "A"
        GENERAL_MILLS = "G"
        KELLOGGS = "K"
        NABISCO = "N"
        POST = "P"
        QUAKER_OATS = "Q"
        RALSTON_PURINA = "R"

    id = UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False
    )

    code = CharField(
        max_length=1,
        choices=ManufacturerChoices.choices,
        null=False
    )

class ThermalType(Model):
    class ThermalChoices(TextChoices):
        COLD = 'C', _("Hot")
        HOT = 'H', _("Cold")
        
    id = UUIDField(
            primary_key=True, 
            default=uuid4, 
            editable=False
        )
    code = CharField(
            max_length=1, 
            choices=ThermalChoices.choices, 
            default=ThermalChoices.COLD, 
            unique=True,
            null=False
        )
    

    
class Cereal(Model):
    name = CharField(max_length=255)
    mfd = ForeignKey(Manufacturer, on_delete=CASCADE)
    type = ForeignKey(ThermalType, on_delete=CASCADE)
    shelf = PositiveIntegerField(null=False, validators=[
        MaxValueValidator(3),
        MinValueValidator(1)
    ])
    weight = FloatField(null=False)
    cups = FloatField(null=False)

class Nutrition(Model):
    cereal = OneToOneField(Cereal, on_delete=CASCADE, primary_key=True)
    calories = PositiveIntegerField(null=False)
    protein = PositiveIntegerField(null=False)
    fat = PositiveIntegerField(null=False)
    sodium = PositiveIntegerField(null=False)
    fiber = FloatField(null=False)
    carbo = FloatField(null=False)
    sugars = PositiveIntegerField(null=False)
    potass = PositiveIntegerField(null=False)
    vitamins = PositiveIntegerField(null=False)
