from django.core.management.base import BaseCommand
from products.models import Manufacturer, ThermalType
from django.db.utils import IntegrityError

# This is a custom command for provisioning the database with the data required for lookup tables (i.e. Manufacturers and thermal types)
# This command is meant to be run only on the initialization of the API


class Command(BaseCommand):

    def handle(self, *args, **options):
        for mfr_code, _ in Manufacturer.ManufacturerChoices.choices:
            try:
                Manufacturer.objects.create(code=mfr_code)
                self.stdout.write(f"Inserted new Manufacturer code: {mfr_code}")
            except IntegrityError:
                self.stderr.write(
                    f"Didn't new Manufacturer code: {mfr_code} - Already exists"
                )
            except:
                self.stderr.write("Something went wrong")

        for thermal_code, _ in ThermalType.ThermalChoices.choices:
            try:
                ThermalType.objects.create(code=thermal_code)
                self.stdout.write(f"Inserted new ThermalType: {thermal_code}")
            except IntegrityError:
                self.stderr.write(
                    f"Didn't insert new ThermalType: {thermal_code} - Already exists"
                )
            except:
                self.stderr.write("Something went wrong")

        self.stdout.write("Finished running provisioning command")
