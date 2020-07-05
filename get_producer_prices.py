import csv


def get_producer_prices(country, from_year, to_year, item_name):
    """
    Get producer price in USD between from_year and to_year inclusive

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
        print_table(('year', 'price_usd'), get_producer_prices(country, 2010, 2019, 'Rice, paddy'))
        print_table(('year', 'price_usd'), get_producer_prices(country, 2010, 2019, 'Sorghum'))
        print_table(('year', 'price_usd'), get_producer_prices(country, 2010, 2019, 'Maize'))
        print_table(('year', 'price_usd'), get_producer_prices(country, 2010, 2019, 'Wheat'))
