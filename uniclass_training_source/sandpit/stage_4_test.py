import os

from uniclass_training_source.sandpit.add_CSV_files_in_path_to_dictionary import add_csv_files_in_path_to_dictionary
from uniclass_training_source.sandpit.export_dataframes_in_a_dictionary_to_csv import \
    export_dataframes_in_a_dictionary_to_csv
from uniclass_training_source.sandpit.uidify_a_dataframe import uuidify_a_dataframe_dictionary

path_of_folder =\
    os.getcwd() + r'\CSV'


test_dictionary = {}

test_list =\
    add_csv_files_in_path_to_dictionary(
        path_of_folder,
        test_dictionary)

uuidify_a_dataframe_dictionary(
    test_dictionary)

export_dataframes_in_a_dictionary_to_csv(
    path_of_folder + r'\test\ ',
    test_dictionary)

print(test_dictionary)



