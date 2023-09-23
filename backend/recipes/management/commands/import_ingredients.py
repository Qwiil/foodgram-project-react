"""Команда для импорта ингредиентов из CSV файла в базу данных."""
import csv
import os

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """Обработка команды."""

    def handle(self, *args, **kwargs):
        """Загрузка ингредиентов из CSV файла в базу данных."""
        current_directory = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(
            current_directory,
            "ingredients.csv",
        )

        with open(csv_file_path, encoding="UTF-8") as ingredients:
            reader = csv.reader(ingredients, delimiter=",")
            for row in reader:
                Ingredient.objects.get_or_create(
                    name=row[0],
                    measurement_unit=row[1],
                )
        self.stdout.write(self.style.SUCCESS("Ингредиенты загружены успешно"))
