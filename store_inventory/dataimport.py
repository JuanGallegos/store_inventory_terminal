import csv


def readfile():
    with open('inventory.csv', newline='') as csvfile:
        prodreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(prodreader)
        return rows


if __name__ == '__main__':
    rows = readfile()
    for row in rows:
        print(row['product_name'])
