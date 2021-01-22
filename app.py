# import datetime
from store_inventory.menu import Menu
from store_inventory.models import Product
from store_inventory.dataimport import DataImporter

# from peewee import *


def main():
    Product().initialize()
    # dimporter = DataImporter()
    # data = dimporter.import_data()
    data = DataImporter().import_data()
    DataImporter().clean_data(data)
    Menu().greeting()
    Menu().menu_display()


if __name__ == '__main__':
    main()
