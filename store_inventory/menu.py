from collections import OrderedDict
from store_inventory.models import Product
from store_inventory.dataimport import DataImporter
import os
import sys


class Menu:
    def __init__(self):
        self.options = OrderedDict([
            ('v', self.display_product),
            ('a', self.add_product),
            ('b', self.backup_database),
            ('c', self.clear),
            ('e', self.exit_menu),
            ])

    def greeting(self):
        self.clear()
        message = '---------------Hello World---------------'
        print('-'*len(message))
        print('-'*len(message))
        print(message)
        print('-'*len(message))
        print('-'*len(message))

    def menu_display(self):
        choice = None
        while True:
            # self.clear()
            for key, value in self.options.items():
                print('{}) {}'.format(key, value.__doc__))
            choice = input('Action: ').lower().strip()

            if choice in self.options:
                # self.clear()
                self.options[choice]()
            else:
                print('That is not a valid selection.')

    def display_product(self):
        '''Display a product by its ID'''
        self.clear()
        id = None
        id = input('Enter the ID to return data: ').lower().strip()
        data = Product().get_product_by_id(id)
        for product in data:
            print(product.product_id,
                  ',', product.product_name,
                  ',', product.product_price,
                  ',', product.product_quantity,
                  ',', product.date_updated)

    def add_product(self):
        '''Add a product to the database'''
        print('Please enter the following information.')
        name = input('Product: ').strip()
        price = input('Price ($8.05): ').lower().strip()
        quantity = input('Quantity (81): ').lower().strip()
        updated = input('Updated Date (12/28/2011): ').lower().strip()
        product = [{'product_name': name,
                    'product_price': price,
                    'product_quantity': quantity,
                    'date_updated': updated
                    },
                   ]
        DataImporter().clean_data(product)

    def backup_database(self):
        '''Backup the database (Export new CSV)'''
        print('backup_database method')

    def exit_menu(self):
        '''Exit Menu'''
        message = 'Thank you for using the Store Inventory application'
        self.clear()
        print('-'*len(message))
        print(message)
        print('-'*len(message))
        sys.exit()

    def clear(self):
        '''Clear Screen'''
        os.system('cls' if os.name == 'nt' else 'clear')
