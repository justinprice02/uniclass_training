import uuid
import pandas

def uuidify_a_dataframe_dictionary(
        dataframe_dictionary: dict
) -> pandas.DataFrame:

    for key in dataframe_dictionary:

        dataframe = \
            dataframe_dictionary[key]


        dataframe['uuid'] = \
            dataframe.apply(lambda _: uuid.uuid4(), axis=1)
