import os
import csv
from django.core.management.base import BaseCommand
from api.models import CryptoData

class Command(BaseCommand):
    help = "Import crypto data from CSV into PostgreSQL"

    def handle(self, *args, **kwargs):
        # Get the absolute path of the CSV file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(base_dir, "")  # Adjust filename if needed

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            crypto_list = []

            for row in reader:
                crypto_list.append(
                    CryptoData(
                        coint_name=row["coin_name"],
                        date=row["date"],
                        open=row["open"],
                        high=row["high"],
                        low=row["low"],
                        close=row["close"],
                        volume=row["volume"],
                    )
                )

            CryptoData.objects.bulk_create(crypto_list)
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(crypto_list)} records!"))
