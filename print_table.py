def print_table(colnames, dicts):
    print('\t'.join(colnames))

    for year in sorted(dicts[-1].keys()):
        print(str(year)+'\t'+'\t'.join([str(i_dict.get(year, '')) for i_dict in dicts]))

    print()


if __name__ == '__main__':
    from get_population_dict import get_population_dict
    from get_producer_price_dict import get_producer_price_dict
    from get_production_tons_dict import get_production_tons_dict

    for country in (
        'Australia',
        'United States of America',
    ):
        for grain in (
            'Rice, paddy',
            'Sorghum',
            'Maize',
            'Wheat'
        ):
            print(country+'\t'+grain)

            producer_price_dict = get_producer_price_dict(country, 2010, 2019, grain)
            production_tons_dict = get_production_tons_dict(country, 2010, 2019, grain)
            usd_gross_dict = {
                year: producer_price_dict[year] * production_tons_dict[year]
                for year in producer_price_dict
            }

            print_table(('year', 'prod_ktons', 'price_usd_kton', 'usd_gross', 'population'), (
                production_tons_dict,
                producer_price_dict,
                usd_gross_dict,
                get_population_dict(country.replace(' of America', ''), 2010, 2019)
            ))
