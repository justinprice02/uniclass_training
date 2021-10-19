import os
import pandas

def export_dataframes_in_a_dictionary_to_csv(
        path_of_export_folder: str,
        dictionary_of_dataframes: dict):

    print(path_of_export_folder)

    for key in dictionary_of_dataframes:
        print(key)
        dictionary_of_dataframes[key].to_csv(path_of_export_folder + key + '.csv')

