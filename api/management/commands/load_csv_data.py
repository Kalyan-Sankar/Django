import csv
import os
from django.core.management import BaseCommand
from api.models import Car

ALREADY_LOADED_MESSAGE="""
If you need to reload the car data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables """

csvfile="/home/kskqpl1/my_projects/django/django_restapi/cars.csv"

class Command(BaseCommand):
    help = "Loads data from cars.csv into our Car model"

    def handle(self, *args, **options):
        if Car.objects.exists():
            print ('Car Data already loaded ...')
            print (ALREADY_LOADED_MESSAGE)
            return

        if os.path.isfile(csvfile):
            with open(csvfile, 'r') as f_csvfile:
                reader=csv.DictReader(f_csvfile, delimiter=',')
                for line in reader:
                    car=Car()
                    car.carmodel=line['model']
                    car.mileage=line['mpg']
                    car.cylinder=line['cyl']
                    car.gear=line['gear']
                    car.save()


