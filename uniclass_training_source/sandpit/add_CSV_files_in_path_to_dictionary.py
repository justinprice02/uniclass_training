import os
import pandas

from uniclass_training_source.sandpit.load_CSV_file_to_dataframe import load_CSV_file_to_dataframe


def add_csv_files_in_path_to_dictionary(
        path_of_folder: str,
        dictionary_name: dict
) -> list:

    list_of_file_names_added = []

    for file in os.listdir(path_of_folder):

         file_name, file_extension = os.path.splitext(file)

         if file_extension == '.csv':

            print(os.path.join(path_of_folder, file))

            dictionary_name[file_name] = \
                load_CSV_file_to_dataframe(
                os.path.join(path_of_folder, file))


            list_of_file_names_added.append(file_name)

    return list_of_file_names_added