from django.core.management.base import BaseCommand
import pandas
from products.models import Product, Manufacturer, ThermalType
from django.db.utils import IntegrityError

# This is a custom command for populating the database with existing data from delivered CSV files.
# This command is only meant to be run on the initialization of the API.


class Command(BaseCommand):
    def handle(self, *args, **options):

        mfr_exists = Manufacturer.objects.first()
        thermal_type_exists = ThermalType.objects.first()
        if not mfr_exists or not thermal_type_exists:
            self.stderr.write("Unable to seed before provision")
            return

        csvFile = pandas.read_csv("data/Cereal.csv", delimiter=";")
        cleaned = csvFile.drop(0)
        for _, data in cleaned.iterrows():
            name = data.get("name")
            mfr_code = data.get("mfr")
            thermal_type_code = data.get("type")
            calories = data.get("calories")
            protein = data.get("protein")
            fat = data.get("fat")
            sodium = data.get("sodium")
            fiber = data.get("fiber")
            carbo = data.get("carbo")
            sugars = data.get("sugars")
            potass = data.get("potass")
            vitamins = data.get("vitamins")
            shelf = data.get("shelf")
            weight = data.get("weight")
            cups = data.get("cups")
            rating = data.get("rating")

            manufacturer = Manufacturer.objects.get(code=mfr_code)
            thermaltype = ThermalType.objects.get(code=thermal_type_code)

            try:
                product = Product.objects.create(
                    name=name,
                    mfr=manufacturer,
                    thermal_type=thermaltype,
                    calories=calories,
                    protein=protein,
                    fat=fat,
                    sodium=sodium,
                    fiber=fiber,
                    carbo=carbo,
                    sugars=sugars,
                    potass=potass,
                    vitamins=vitamins,
                    shelf=shelf,
                    weight=weight,
                    cups=cups,
                    rating=rating,
                )
                self.stdout.write(f"Inserted new Product: {product.name}")
            except IntegrityError:
                self.stderr.write(f"Skipping - Product: {name} already exists")
            except Exception as e:
                self.stderr.write(f"Something went wrong: {e}")
