from collections import OrderedDict
from store_inventory.models import Product
from store_inventory.dataimport import DataImporter
from store_inventory.dataexport import DataExporter
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
        message = '------ Hello, Welcome to Store Inventory Application ------'
        print('-'*len(message))
        print('-'*len(message))
        print(message)
        print('-'*len(message))
        print('-'*len(message))
        print()

    def menu_display(self):
        choice = None
        while True:
            print('-'*50)
            print('Please make your selection from the options below:')
            print('-'*50)
            # self.clear()
            for key, value in self.options.items():
                print('{}) {}'.format(key, value.__doc__))
            choice = input('Action: ').lower().strip()

            if choice in self.options:
                # self.clear()
                self.options[choice]()
            else:
                self.clear()
                print('-'*50)
                print(f'\'{choice}\' is not a valid selection.')
                print('-'*50)
                input('Press Enter to Continue.')
                self.clear()

    def display_product(self):
        '''Display a product by its ID'''
        self.clear()
        id = None
        print('-'*50)
        id = input('Enter the ID to return data: ').lower().strip()
        print('-'*50)
        data = Product().get_product_by_id(id)
        for product in data:
            print(product.product_id,
                  ',', product.product_name,
                  ',', product.product_price,
                  ',', product.product_quantity,
                  ',', product.date_updated)
        print('-'*50)
        input('Press Enter to Continue.')
        self.clear()

    def add_product(self):
        '''Add a product to the database'''
        print('Please enter the following information.')
        name = input('Product: ').strip()
        price = input('Price ($8.05): ').lower().strip()
        quantity = input('Quantity (81): ').lower().strip()
        updated = None
        product = [{'product_name': name,
                    'product_price': price,
                    'product_quantity': quantity,
                    'date_updated': updated
                    },
                   ]
        DataImporter().clean_data(product)

    def backup_database(self):
        '''Backup the database (Export new CSV)'''
        DataExporter().backup_database()
        self.clear()
        print('-'*50)
        print('Your backup file has been created.')
        print('-'*50)
        input('Press Enter to Continue.')
        self.clear()

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
