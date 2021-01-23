from store_inventory.menu import Menu
from store_inventory.models import Product
from store_inventory.dataimport import DataImporter


def main():
    Product().initialize()
    data = DataImporter().import_data()
    DataImporter().clean_data(data)
    Menu().menu_display()


if __name__ == '__main__':
    main()
