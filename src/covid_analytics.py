from covid_data import *
import pandas as pd
def main():
    #print(pd.show_versions())
    #print(CovidData.get_covid_primary_data())
    #print(CovidData.get_covid_primary_data()\
    #    .info("verbose"))
    #print(CovidData.get_county_employment())
    #print(CovidData.get_county_hospital())
    CovidData.get_covid_primary_data()
    
main()
