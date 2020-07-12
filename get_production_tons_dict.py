import csv


def get_production_tons_dict(country, from_year, to_year, item_name):
    """
    Get production in kilotonnes between from_year and to_year inclusive

    :param country: the country name (not code),
                    e.g. "Australia" or "United States"
    :param from_year:
    :param to_year:
    :param item_name: e.g. "Maize"
    :return: a dict of {year: production amount in ktonnes, ...}
    """
    r = {}

    with open('data/faostat_data_2020_6_7.csv', 'r', encoding='utf-8') as f:
        for item in csv.DictReader(f):
            if item['Area'].lower() != country.lower():
                continue
            elif not (from_year <= int(item['Year']) <= to_year):
                continue
            elif item['Item'].lower() != item_name.lower():
                continue

            r[int(item['Year'])] = int(item['Value'])

    return r

