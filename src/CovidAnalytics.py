from CovidData import *

def main():
    print(CovidData.getCovidPrimaryData())
    print(CovidData.getCovidPrimaryData()\
          .info("verbose"))
    
main()
