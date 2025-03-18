import pandas as pd

class DataPreprocessor:
    # This class is meant to store cleaning and processing tasks
    def __init__(self, df_fact, df_dim):
        self.df_fact = df_fact
        self.df_dim = df_dim

    def unpivot_columns(self, id_vars, value_vars, var_name="Year", value_name="Popullation"):
        # unpivot table to get years as columns
        # id_vars are columns to keep fixed
        # value vars are the columns to be unpivoted
        self.df_fact = pd.melt(self.df_fact, id_vars, value_vars, var_name, value_name)
        return self.df_fact
    
    def join_data(self, join_key, how="left"):
        # Joins country dim data
        self.df_fact.merge(self.df_dim, on=join_key, how=how)
        return self.df_fact

