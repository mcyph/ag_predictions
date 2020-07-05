def print_table(colnames, vals):
    print('\t'.join(colnames))

    for i_vals in vals:
        print('\t'.join(str(i) for i in i_vals))

    print()
