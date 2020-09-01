import pandas as pd

class CovidData:
    
    # Primary data paths.
    _covid_cases_path = "../data/Covid/covid_confirmed_usafacts.csv"
    _covid_population_path = "../data/Covid/covid_county_population_usafacts.csv"
    _covid_death_path = "../data/Covid/covid_deaths_usafacts.csv"
    # Extension data paths.
    _county_employment_path = "../data/Employment/county-ests-employment-and-wages.csv"
    _county_hospital_path = "../data/Hospitals/Definitive_Healthcare _USA_Hospital_Beds.csv"

    @staticmethod
    def get_covid_by_cases():
        return pd.read_csv(CovidData._covid_cases_path)

    @staticmethod
    def get_county_population():
        return pd.read_csv(CovidData._covid_population_path)

    @staticmethod
    def get_covid_by_deaths():
        return pd.read_csv(CovidData._covid_death_path)

    @staticmethod
    def get_covid_primary_data():
        first_merge = pd.merge(CovidData.get_covid_by_cases(), \
                              CovidData.get_covid_by_population(), \
                              how = "inner")
        second_merge = pd.merge(first_merge, \
                               CovidData.get_covid_by_deaths(), \
                               how = "inner")
        return first_merge

    @staticmethod
    def get_county_employment():
        return pd.read_csv(CovidData._county_employment_path)

    @staticmethod
    def get_county_hospital():
        return pd.read_csv(CovidData._county_hospital_path)
