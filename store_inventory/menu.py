from collections import OrderedDict
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
        print('---------------------------')
        print('---------------------------')
        print('------Hello World----------')
        print('---------------------------')
        print('---------------------------')

    def menu_display(self):
        choice = None
        while choice != 'q':
            # self.clear()
            print('Enter \'q\' to quit.')
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
        print('display_product method')

    def add_product(self):
        '''Add a product to the database'''
        print('add_product method')

    def backup_database(self):
        '''Backup the database (Export new CSV)'''
        print('backup_database method')

    def exit_menu(self):
        '''Exit Menu'''
        print('exit_menu method')

    def clear(self):
        '''Clear Screen'''
        os.system('cls' if os.name == 'nt' else 'clear')


# if __name__ == '__main__':
#     menu = Menu()
#     menu.greeting()
#     menu.menu_display()
