from pandas import DataFrame


def strains(df: DataFrame):
    return df['Strain']


def compound_abundance(no: int, df: DataFrame):
    col_name = f'compound {no}'
    return df[col_name]


def count_compounds(df: DataFrame) -> int:
    compound_cols = [col for col in df.columns if col.startswith('compound')]
    return len(compound_cols)
