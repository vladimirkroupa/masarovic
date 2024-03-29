import itertools

from pandas import DataFrame

import sheet


def convert_dataframe(df: DataFrame) -> DataFrame:
    compound_cnt = sheet.count_compounds(df)

    strain_col = sheet.strains(df)
    strain_cnt = len(strain_col)

    new_strain_col = []
    new_compound_no_col = []
    new_abundance_col = []

    for comp_no in range(1, compound_cnt + 1):
        compound_no_col = itertools.repeat(comp_no, strain_cnt)
        abundance_col = sheet.compound_abundance(comp_no, df)

        new_strain_col = itertools.chain(new_strain_col, strain_col)
        new_compound_no_col = itertools.chain(new_compound_no_col, compound_no_col)
        new_abundance_col = itertools.chain(new_abundance_col, abundance_col)

    strain_compound_abundance = zip(new_strain_col, new_compound_no_col, new_abundance_col)
    return DataFrame(strain_compound_abundance, columns=['Strain', 'Compound', 'Abundance'])
