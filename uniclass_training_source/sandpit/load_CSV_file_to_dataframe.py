import os
import pandas

def load_CSV_file_to_dataframe (
        file_name_and_path: str
) -> pandas.DataFrame:

    data_frame_from_CSV = \
        pandas.read_csv(file_name_and_path, encoding='cp1252')

    return data_frame_from_CSV