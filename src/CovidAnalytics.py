from CovidData import *

def main():
    print(CovidData.getCovidPrimaryData())
    print(CovidData.getCovidPrimaryData()\
          .info("verbose"))
    print(CovidData.getCountyEmployment())
    print(CovidData.getCountyHospital())
    
main()
