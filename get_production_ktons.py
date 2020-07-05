import csv


def get_production_ktons(country, from_year, to_year, item_name):
    """
    Get production in kilotonnes between from_year and to_year inclusive

    :param country: the country name (not code),
                    e.g. "Australia" or "United States"
    :param from_year:
    :param to_year:
    :param item_name:
    :return: a two-tuple of ((year, production amount in ktonnes), ...)
    """
    r = []

    with open('data/faostat_data_2020_6_7.csv', 'r', encoding='utf-8') as f:
        for item in csv.DictReader(f):
            if item['Area'].lower() != country.lower():
                continue
            elif not (from_year <= int(item['Year']) <= to_year):
                continue
            elif item['Item'].lower() != item_name.lower():
                continue

            r.append((int(item['Year']), int(item['Value'])/1000.0))

    return r


if __name__ == '__main__':
    from print_table import print_table

    for country in (
        'Australia',
        'United States of America',
    ):
        print_table(('year', 'prod_ktons'), get_production_ktons(country, 2010, 2019, 'Rice, paddy'))
        print_table(('year', 'prod_ktons'), get_production_ktons(country, 2010, 2019, 'Sorghum'))
        print_table(('year', 'prod_ktons'), get_production_ktons(country, 2010, 2019, 'Maize'))
        print_table(('year', 'prod_ktons'), get_production_ktons(country, 2010, 2019, 'Wheat'))
