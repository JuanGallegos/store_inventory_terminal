from csv import DictWriter
from store_inventory.models import Product


class DataExporter:
    def backup_database(self):
        '''Creates a CSV backup of Inventory database'''
        export_data = 'export_data/inventory_back.csv'
        with open(export_data, 'w') as export_file:
            fields = ['product_name',
                      'product_price',
                      'product_quantity',
                      'date_updated']
            export_writer = DictWriter(export_file, fieldnames=fields)

            export_writer.writeheader()
            products = Product.select()
            for product in products:
                export_writer.writerow({
                    'product_name': product.product_name,
                    'product_price': product.product_price,
                    'product_quantity': product.product_quantity,
                    'date_updated': product.date_updated,
                })
