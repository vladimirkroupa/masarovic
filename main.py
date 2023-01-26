from pandas import DataFrame, ExcelFile

import processor


def transform_sheet(filename: str, source_sheet_name: str):
    xls = ExcelFile(filename)
    source_df: DataFrame = xls.parse(source_sheet_name)
    processor.process_dataframe(source_df)


if __name__ == '__main__':
    transform_sheet('Strains-R.xlsx', 'original matrix')
