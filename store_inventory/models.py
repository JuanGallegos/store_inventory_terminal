import datetime
from peewee import (
    Model,
    PrimaryKeyField,
    CharField,
    IntegerField,
    DateTimeField,
    SqliteDatabase)

db = SqliteDatabase('inventory.db')


class Product(Model):
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255, unique=True)
    product_price = IntegerField()
    product_quantity = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def initialize(self):
        """Create the database and table if they do not exist."""
        db.connect()
        db.create_tables([Product], safe=True)

    def get_product_by_name(self, name):
        '''Returns products where product_name contains name'''
        products = Product.select().order_by(Product.date_updated.desc())
        products = products.where(Product.product_name.contains(name))
        return products

    def get_product_by_id(self, id):
        '''Returns products where product_name contains name'''
        products = Product.select().where(Product.product_id == id)
        return products

    def update_entry_using_query(self, product, price, quantity, updated):
        '''
        Query and retrieve an object by ID and then update product details
        '''
        pdetails = Product.select()
        pdetails.where(Product.product_id == product.product_id)
        pdetails.get()
        pdetails.product_price = price
        pdetails.product_quantity = quantity
        pdetails.date_updated = updated
        pdetails.save()

    def update_entry(self, product, price, quantity, updated):
        '''Use update statement to update product details where product_id'''
        q = Product.update(product_price=price,
                           product_quantity=quantity,
                           date_updated=updated
                           ).where(Product.product_id == product.product_id)
        q.execute()
