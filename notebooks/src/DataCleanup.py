import pandas as pd

class datacleaner:
    "This class cleans the world bank popullation dataset"

    def __init__(self, df):
        self.df = df

    def column_dropper(self):
        "This function drops "

    def na_cc_dropper(self):
        "This function drops INX and PSE country codes"
        self.df =(
            self.df[self.df["Country Code"].isin(["INX", "PSE"])]      
            )
        