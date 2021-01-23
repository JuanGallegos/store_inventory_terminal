from collections import OrderedDict
import os
import sys
from store_inventory.models import Product
from store_inventory.dataimport import DataImporter
from store_inventory.dataexport import DataExporter


class Menu:
    def __init__(self):
        self.options = OrderedDict([
            ('v', self.display_product),
            ('a', self.add_product),
            ('b', self.backup_database),
            ('e', self.exit_menu),
            ])

    def greeting(self):
        '''Welcome message to Inventory Application'''
        self.clear()
        message = '------- Welcome to the Store Inventory Application -------'
        print('-'*len(message))
        print('-'*len(message))
        print(message)
        print('-'*len(message))
        print('-'*len(message))

    def end_message_after_action(self):
        '''Output after completion of chosen menu option.'''
        print('-'*70)
        input('Press Enter to Continue.')
        self.clear()

    def menu_display(self):
        '''Menu Display.'''
        choice = None
        self.greeting()
        while True:
            print('Please make your selection from the options below:')

            for key, value in self.options.items():
                print('{}) {}'.format(key, value.__doc__))
            choice = input('Action: ').lower().strip()

            if choice in self.options:
                self.options[choice]()
            else:
                self.clear()
                print('-'*70)
                print(f'\'{choice}\' is not a valid selection.')
                self.end_message_after_action()

    def display_product(self):
        '''Display a product by its ID'''
        id = None
        self.clear()
        print('-'*70)

        try:
            id = input('Enter the ID to return data: ').lower().strip()
            print('-'*70)
            data = Product().get_product_by_id(id)

            if not data.exists():
                print('There is no data associated to that ID.')
            else:
                for product in data:
                    print(product.product_id,
                          ',', product.product_name,
                          ',', '${:.2f}'.format(product.product_price/100),
                          ',', product.product_quantity,
                          ',', product.date_updated)
            self.end_message_after_action()

        except ValueError:
            print('This is not a valid ID.')
            self.end_message_after_action()

    def add_product(self):
        '''Add a product to the database'''
        self.clear()
        print('-'*70)
        print('Please enter the following information.')
        print('-'*70)
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

        print('-'*70)

        try:
            DataImporter().clean_data(product)
        except ValueError:
            print('You entered a product that does not follow the format.')
            self.end_message_after_action()
        else:
            print('Your entry has been recorded.')
            self.end_message_after_action()

    def backup_database(self):
        '''Backup the database (Export new CSV)'''
        DataExporter().backup_database()
        self.clear()
        print('-'*70)
        print('Your backup file has been created.')
        self.end_message_after_action()

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
