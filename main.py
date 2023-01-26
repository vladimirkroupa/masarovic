from pandas import DataFrame, ExcelFile

import processor


def transform_sheet(source_filename: str, source_sheet_name: str, target_filename: str, target_sheet_name: str):
    xls = ExcelFile(source_filename)
    source_df: DataFrame = xls.parse(source_sheet_name)
    new_df = processor.convert_dataframe(source_df)
    store_as_xls(new_df, target_filename, target_sheet_name)


def store_as_xls(df: DataFrame, xls_file_name: str, sheet_name: str):
    df.to_excel(xls_file_name, sheet_name=sheet_name, index=False)


if __name__ == '__main__':
    transform_sheet('Strains-R.xlsx', 'original matrix', 'Strains-R-out.xlsx', 'Output')
