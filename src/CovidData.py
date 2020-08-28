import csv
import pandas as pd
class CovidData:
    
    # Primary data paths.
    _covidCasesPath = "../data/Covid/covid_confirmed_usafacts.csv"
    _covidPopulationPath = "../data/Covid/covid_county_population_usafacts.csv"
    _covidDeathPath = "../data/Covid/covid_deaths_usafacts.csv"
    # Extension data paths.
    _countyEmploymentPath = "../data/Employment/county-ests-employment-and-wages.csv"
    _CountyHospitalPath = "../Data/Hospitals/Definitive_Healthcare _USA_Hospital_Beds.csv"

    @staticmethod
    def getCovidByCases():
        return pd.read_csv(CovidData._covidCasesPath)

    @staticmethod
    def getCovidByPopulation():
        return pd.read_csv(CovidData._covidPopulationPath)

    @staticmethod
    def getCovidByDeaths():
        return pd.read_csv(CovidData._covidDeathPath)

    @staticmethod
    def getCovidPrimaryData():
        firstMerge = pd.merge(CovidData.getCovidByCases(), \
                              CovidData.getCovidByPopulation(), \
                              how = "inner")
        secondMerge = pd.merge(firstMerge, \
                               CovidData.getCovidByDeaths(), \
                               how = "inner")
        return firstMerge

    @staticmethod
    def getCountyEmployment():
        return pd.read_csv(CovidData._countyEmploymentPath)

    @staticmethod
    def getCountyHospital():
        return pd.read_csv(CovidData._countyHopsitalPath)
