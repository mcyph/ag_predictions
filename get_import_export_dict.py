import csv
from collections import namedtuple


ImportExportItem = namedtuple('ImportExportItem', [
    'import_quantity',
    'import_value',
    'export_quantity',
    'export_value'
])


def get_import_export_dict(country, from_year, to_year, item_name):
    """
    Get import/export quantity/value
    between from_year and to_year inclusive

    :param country: the country name (not code),
                    e.g. "Australia" or "United States"
    :param from_year:
    :param to_year:
    :param item_name: e.g. "Rice, Paddy"
    :return: a dict of {year: ImportExportItem instance, ...}
    """
    r = {}

    mapping = {
        'Import Quantity': 'import_quantity',
        'Export Quantity': 'export_quantity',
        'Import Value': 'import_value',
        'Export Value': 'export_value',
    }

    with open('data/faostat_import_export_data.csv', 'r', encoding='utf-8') as f:
        for item in csv.DictReader(f):
            if item['Area'].lower() != country.lower():
                continue
            elif not (from_year <= int(item['Year']) <= to_year):
                continue
            elif item['Item'].lower() != item_name.lower():
                continue

            r.setdefault(int(item['Year']), {
                k: None for k in mapping.values()
            })[mapping[item['Element']]] = \
                float(item['Value'])

    return {
        k: ImportExportItem(**v)
        for k, v in r.items()
    }


if __name__ == '__main__':
    print(get_import_export_dict('Australia', 2000, 2010, 'Wheat'))
