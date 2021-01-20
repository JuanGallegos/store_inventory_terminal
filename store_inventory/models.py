import datetime
from peewee import Model, PrimaryKeyField, CharField, IntegerField, DateTimeField, SqliteDatabase

db = SqliteDatabase('inventory.db')

class Product(Model):
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255, unique=True)
    product_price = IntegerField()
    product_quantity = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
