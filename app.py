import datetime
from store_inventory.menu import Menu
from store_inventory.models import Product, db
from store_inventory.dataimport import readfile

from peewee import *


def initialize():
    """Create the database and table if they do not exist."""
    db.connect()
    db.create_tables([Product], safe=True)


def import_data():
    rows = readfile()
    return rows


def clean_data(rows):
    for row in rows:
        name = row['product_name']
        price = int(row['product_price'].replace(
                '$', '').replace('.', ''))
        quantity = int(row['product_quantity'])
        updated = datetime.datetime.strptime(row['date_updated'], '%m/%d/%Y')
        try:
            add_entry(name, price, quantity, updated)
        except IntegrityError:
            address_duplicates(name, price, quantity, updated)


def add_entry(product_name, product_price, product_quantity, date_updated):
    """Add an entry"""
    Product.create(product_name=product_name,
                   product_price=product_price,
                   product_quantity=product_quantity,
                   date_updated=date_updated)
    # print('Saved successfully!')


def get_product_by_name(name):
    '''Returns products where product_name contains name'''
    products = Product.select().order_by(Product.date_updated.desc())
    products = products.where(Product.product_name.contains(name))
    return products


def update_entry_using_query(product, price, quantity, updated):
    '''Query and retrieve an object by ID and then update product details'''
    pdetails = Product.select().where(Product.product_id == product.product_id)
    pdetails.get()
    pdetails.product_price = price
    pdetails.product_quantity = quantity
    pdetails.date_updated = updated
    pdetails.save()


def update_entry(product, price, quantity, updated):
    '''Use update statement to update product details where product_id'''
    q = Product.update(product_price=price,
                       product_quantity=quantity,
                       date_updated=updated
                       ).where(Product.product_id == product.product_id)
    q.execute()


def address_duplicates(name, price, quantity, updated):
    '''
    Gets products and checks whether there is duplicates.
    If there are duplicates, then a method is called to save the data
    with the most recent data in the existing record.
    '''
    products = get_product_by_name(name)
    for product in products:
        if product.date_updated < updated:
            #print(product.date_updated, 'is less than', updated)
            update_entry(product, price, quantity, updated)
        else:
            #print(product.date_updated, 'is greater than', updated)
            continue


# Connect the database and create tables
# in dunder method
if __name__ == '__main__':
    initialize()
    data = import_data()
    clean_data(data)
    menu = Menu()
    menu.greeting()
    menu.menu_display()
