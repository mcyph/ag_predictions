import json


def __output_population_json(iso_code, population_dict):
    """

    :param iso_code:
    :param population_dict:
    :return:
    """
    with open(
        f'output/{iso_code}_population.json',
        'w', encoding='utf-8'
    ) as f:
        output = {
            'country': iso_code,
            'population': [
                {
                    'year': year,
                    'value': population
                }
                for year, population
                in sorted(population_dict.items(), reverse=True)
            ]
        }
        f.write(json.dumps(
            output, indent=4, ensure_ascii=False
        ))


def __output_crop_json(iso_code, normalized_grain,
                       producer_price_dict,
                       production_ktons_dict,
                       usd_gross_dict):
    """

    :param normalized_grain:
    :param iso_code:
    :param producer_price_dict:
    :param production_ktons_dict:
    :return:
    """
    with open(
            f'output/{iso_code}_{normalized_grain.lower()}.json',
            'w', encoding='utf-8'
    ) as f:
        years = set()
        years.update(producer_price_dict)
        years.update(production_ktons_dict)
        years.update(usd_gross_dict)

        output = {
            'country': iso_code,
            'crop': normalized_grain,
            'unit': 't',
            'production': [
                {
                    'year': year,
                    'quantity': production_ktons_dict.get(year),
                    'priceUSD': producer_price_dict.get(year),
                    'totalValueUSD': usd_gross_dict.get(year)
                }
                for year in sorted(years, reverse=True)
            ]
        }
        f.write(json.dumps(
            output, indent=4, ensure_ascii=False
        ))


if __name__ == '__main__':
    from get_population_dict import get_population_dict
    from get_producer_price_dict import get_producer_price_dict
    from get_production_tons_dict import get_production_tons_dict

    for country, iso_code in (
        ('Australia', 'au'),
        ('United States of America', 'us'),
    ):
        for grain, normalized_grain in (
            ('Rice, paddy', 'Rice'),
            ('Sorghum', 'Sorghum'),
            ('Maize', 'Corn'),
            ('Wheat', 'Wheat'),
            ('Barley', 'Barley'),
        ):
            print(country+'\t'+grain)

            producer_price_dict = get_producer_price_dict(country, 2010, 2019, grain)
            production_tons_dict = get_production_tons_dict(country, 2010, 2019, grain)
            usd_gross_dict = {
                year: producer_price_dict[year] * production_tons_dict[year]
                for year in producer_price_dict
            }
            population_dict = get_population_dict(country.replace(' of America', ''), 2010, 2019)

            __output_population_json(
                iso_code, population_dict
            )
            __output_crop_json(
                iso_code, normalized_grain,
                producer_price_dict,
                production_tons_dict,
                usd_gross_dict
            )
