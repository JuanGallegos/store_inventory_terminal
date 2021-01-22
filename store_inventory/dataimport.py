import csv
import datetime
from store_inventory.models import Product, db
from peewee import *


class DataImporter:
    def __init__(self):
        pass

    def import_data(self):
        rows = self.readfile()
        return rows

    def readfile(self):
        with open('inventory.csv', newline='') as csvfile:
            prodreader = csv.DictReader(csvfile, delimiter=',')
            rows = list(prodreader)
            return rows

    def clean_data(self, rows):
        for row in rows:
            name = row['product_name']
            price = int(row['product_price'].replace(
                    '$', '').replace('.', ''))
            quantity = int(row['product_quantity'])
            updated = datetime.datetime.strptime(
                row['date_updated'], '%m/%d/%Y')
            try:
                Product().add_import_entry(name, price, quantity, updated)
            except IntegrityError:
                pass
                self.address_duplicates(name, price, quantity, updated)

    def address_duplicates(self, name, price, quantity, updated):
        '''
        Gets products and checks whether there is duplicates.
        If there are duplicates, then a method is called to save the data
        with the most recent data in the existing record.
        '''
        products = Product().get_product_by_name(name)
        for product in products:
            if product.date_updated < updated:
                # print(product.date_updated, 'is less than', updated)
                Product().update_entry(product, price, quantity, updated)
            else:
                # print(product.date_updated, 'is greater than', updated)
                continue


if __name__ == '__main__':
    rows = DataImporter.readfile()
    for row in rows:
        print(row['product_name'])
