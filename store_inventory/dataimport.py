import csv
import datetime
from store_inventory.models import Product
from peewee import IntegrityError


class DataImporter:
    def __init__(self):
        pass

    def import_data(self):
        rows = self.readfile()
        return rows

    def readfile(self):
        with open('import_data/inventory.csv', newline='') as csvfile:
            prodreader = csv.DictReader(csvfile, delimiter=',')
            rows = list(prodreader)
            return rows

    def clean_data(self, rows):
        for row in rows:
            name = row['product_name']
            price = int(row['product_price'].replace(
                    '$', '').replace('.', ''))
            quantity = int(row['product_quantity'])
            if row['date_updated'] is not None:
                updated = datetime.datetime.strptime(
                    row['date_updated'], '%m/%d/%Y')
            else:
                updated = datetime.datetime.now()

            try:
                self.add_import_entry(name, price, quantity, updated)
            except IntegrityError:
                pass
                self.address_duplicates(name, price, quantity, updated)

    def add_import_entry(self, product_name, product_price,
                         product_quantity, date_updated):
        """Add an entry"""
        Product.create(product_name=product_name,
                       product_price=product_price,
                       product_quantity=product_quantity,
                       date_updated=date_updated)
        # print('Saved successfully!')

    def address_duplicates(self, name, price, quantity, updated):
        '''
        Gets products and checks whether there is duplicates.
        If there are duplicates, then a method is called to save the data
        with the most recent data in the existing record.
        '''
        products = Product().get_product_by_name(name)
        for product in products:
            if product.date_updated < updated:
                print(product.date_updated, 'is less than', updated)
                print('The existing product will be updated with this record')
                Product().update_entry(product, price, quantity, updated)
            else:
                # print(product.date_updated, 'is greater than', updated)
                continue
