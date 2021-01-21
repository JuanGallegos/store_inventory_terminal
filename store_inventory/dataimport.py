import csv


class DataImporter:
    def __init__(self):
        pass

    def readfile(self):
        with open('inventory.csv', newline='') as csvfile:
            prodreader = csv.DictReader(csvfile, delimiter=',')
            rows = list(prodreader)
            return rows

    def import_data(self):
        rows = self.readfile()
        return rows


if __name__ == '__main__':
    rows = DataImporter.readfile()
    for row in rows:
        print(row['product_name'])
