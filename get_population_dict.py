import csv


def get_population_dict(country, from_year, to_year):
    """
    Get the population of a country

    :param country: the country name (not code),
                    e.g. "Australia" or "United States"
    :param from_year:
    :param to_year:
    :return: a two-tuple of ((year, population), ...)
    """

    r = {}

    with open('data/world_bank_popdata.csv', 'r', encoding='utf-8-sig') as f:
        for item in csv.DictReader(f):
            if item['Country Name'].lower() != country.lower():
                continue

            for k, v in item.items():
                # Columns are years
                try:
                    int(k)
                except ValueError:
                    continue

                if not (from_year <= int(k) <= to_year):
                    continue

                r[int(k)] = int(v)

    return r

