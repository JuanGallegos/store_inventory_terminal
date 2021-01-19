import datetime

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


# Connect the database and create tables
# in dunder method
if __name__ == '__main__':
    initialize()
    # 2. Ensure you load the CSV products data into the created table
    # 3. Run the app so that use can make menu choices and interact w/ app
