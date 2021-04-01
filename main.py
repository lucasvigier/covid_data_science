import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

country_list = ["Italy", "Spain", "France", "United Kingdom", "US", "India", "Belgium", "Russia", "Netherlands",
                "Bangladesh"]

confirmed_df = pd.read_csv('csv/time_series_covid19_confirmed_global.csv', index_col=0)
confirmed_df.set_index("Country/Region", inplace=True)
deaths_df = pd.read_csv('csv/time_series_covid19_deaths_global.csv', index_col=0)
deaths_df.set_index("Country/Region", inplace=True)
recovered_df = pd.read_csv('csv/time_series_covid19_recovered_global.csv', index_col=0)
recovered_df.set_index("Country/Region", inplace=True)

data_confirmed = confirmed_df.loc[country_list].iloc[:, 5:]
data_deaths = deaths_df.loc[country_list].iloc[:, 5:]
data_recovered = recovered_df.loc[country_list].iloc[:, 5:]

print("##################################### Question 1 #####################################")
confirmed_array = data_confirmed.loc[country_list].iloc[:, -1:]
deaths_array = data_deaths.loc[country_list].iloc[:, -1:]
recovered_array = data_recovered.loc[country_list].iloc[:, -1:]

data_array = pd.concat([confirmed_array, deaths_array, recovered_array], axis=1)
data_array.columns = ['confirmed', 'deaths', 'recovered']
patterns = {'confirmed': 'sum', 'deaths': 'sum', 'recovered': 'sum'}
array = data_array.groupby("Country/Region").aggregate(patterns)
print(array)
print("######################################################################################")
print()
print("#################################### Question 2.a ####################################")
for country in country_list:
    if data_confirmed.loc[country].ndim > 1:
        confirmed_graph = data_confirmed.loc[country].sum().diff()
        deaths_graph = data_deaths.loc[country].sum().diff()
        recovered_graph = data_recovered.loc[country].sum().diff()
    else:
        confirmed_graph = data_confirmed.loc[country].diff()
        deaths_graph = data_deaths.loc[country].diff()
        recovered_graph = data_recovered.loc[country].diff()
    graph = pd.DataFrame([confirmed_graph, deaths_graph, recovered_graph]).transpose()
    graph.columns = ["confirmed", "deaths", "recovered"]
    graph.plot()
    plt.title(country, size=12)
    print("Plotting the graph of:", country)
    plt.show()
print("######################################################################################")
print()
print("#################################### Question 2.b ####################################")
for country in country_list:
    if data_confirmed.loc[country].ndim > 1:
        confirmed_graph = data_confirmed.loc[country].sum()
        deaths_graph = data_deaths.loc[country].sum()
        recovered_graph = data_recovered.loc[country].sum()
    else:
        confirmed_graph = data_confirmed.loc[country]
        deaths_graph = data_deaths.loc[country]
        recovered_graph = data_recovered.loc[country]
    print("Plotting the graph of confirmed data for:", country)
    confirmed_graph.plot()
    plt.title(country + " : confirmed", size=12)
    plt.show()
    print("Plotting the graph of deaths data for:", country)
    deaths_graph.plot()
    plt.title(country + " : deaths", size=12)
    plt.show()
    print("Plotting the graph of recovered data for:", country)
    recovered_graph.plot()
    plt.title(country + " : recovered", size=12)
    plt.show()
    print()
print("######################################################################################")
print()
print("#################################### Question 2.c ####################################")
confirmed_graph = data_confirmed.groupby("Country/Region").aggregate('sum').transpose()
print("Plotting the graph of confirmed data for all countries")
confirmed_graph.plot()
plt.title("All countries : confirmed", size=12)
plt.show()
print("######################################################################################")
print()
print("#################################### Question 2.d ####################################")
deaths_graph = data_deaths.groupby("Country/Region").aggregate('sum').transpose()
print("Plotting the graph of deaths data for all countries")
deaths_graph.plot()
plt.title("All countries : deaths", size=12)
plt.show()
print("######################################################################################")
print()
print("#################################### Question 2.e ####################################")
recovered_graph = data_recovered.groupby("Country/Region").aggregate('sum').transpose()
print("Plotting the graph of recovered data for all countries")
recovered_graph.plot()
plt.title("All countries : recovered", size=12)
plt.show()
print("######################################################################################")
