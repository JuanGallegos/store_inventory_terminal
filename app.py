import datetime

from dataimport import readfile

from peewee import *


db = SqliteDatabase('inventory.db')


class Product(Model):
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255, unique=True)
    product_price = IntegerField()
    product_quantity = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and table if they do not exist."""
    db.connect()
    db.create_tables([Product], safe=True)


def add_entry(product_name, product_price, product_quantity, date_updated):
    """Add an entry"""
    Product.create(product_name=product_name,
                   product_price=product_price,
                   product_quantity=product_quantity,
                   date_updated=date_updated)
    print('Saved successfully!')


# Connect the database and create tables
# in dunder method
if __name__ == '__main__':
    initialize()
    rows = readfile()
    for row in rows:
        name = row['product_name']
        price = int(row['product_price'].replace(
                '$', '').replace('.', ''))
        quantity = int(row['product_quantity'])
        updated = datetime.datetime.strptime(row['date_updated'], '%m/%d/%Y')
        try:
            add_entry(name, price, quantity, updated)
        except IntegrityError:
            print(f'You\'re trying to duplicate "{name}" which has a unique key.')
            print(name,
                  price,
                  quantity,
                  updated)
            products = Product.select().order_by(Product.date_updated.desc())
            products = products.where(Product.product_name.contains(name))
            for product in products:
                # print(product.product_id,
                #       product.product_name,
                #       product.product_price,
                #       product.product_quantity,
                #       product.date_updated)
                if product.date_updated > updated:
                    print(product.date_updated, 'is greater than', updated)
                else:
                    print(product.date_updated, 'is less than', updated)
                    # Using a query to retrieve an object
                    # pdetails = Product.select().where(Product.product_id == product.product_id).get()
                    # pdetails.product_price = price
                    # pdetails.product_quantity = quantity
                    # pdetails.date_updated = updated
                    # pdetails.save()

                    # Using update to update object
                    Product.update(product_price=price,
                                   product_quantity=quantity,
                                   date_updated=updated
                                   ).where(Product.product_id
                                           == product.product_id).execute()
