import pandas as pd

class DataPreprocessor:
    # This class is meant to store cleaning and processing tasks
    def __init__(self, df_fact, df_dim):
        self.df_fact = df_fact
        self.df_dim = df_dim

    def unpivot_columns(self, id_vars, value_cars, var_name="Year", value_name="Popullation"):
        # unpivot table to get years as columns
        # id_vars are columns to keep fixed
        # value vars are the columns to be unpivoted
        self.df_fact = pd.melt