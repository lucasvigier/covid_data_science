import numpy as np
import pandas as pd

country_list = ["Italy", "Spain", "France", "United Kingdom", "US", "India", "Belgium", "Russia", "Netherlands", "Bangladesh"]
total_confirmed_csv = pd.read_csv('csv/time_series_covid19_confirmed_global.csv', index_col=0)

def total_confirmed_country(df):
    df.set_index("Country/Region", inplace=True)
    result = df.loc[country_list]
    print(result)

total_confirmed_country(total_confirmed_csv)