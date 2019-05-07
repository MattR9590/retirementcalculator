#retirement calculator

import sys 
import math

def main():
	print(' ***PYTHON V3 RETIREMENT CALCULATOR***')

	currentAge = input('What is your current age?: ')
	ageRetirement = input('What age do you plane to retire?: ')
	houseIncome = input('What is your household income?: ')
	annualSavingsrate = input('What is you annual savings rate percent?: ')
	currentSavings = input('Current retirement savings?: ')
	incomeIncrease = input('Expected income increase (percent): ')
	incomeRetirement = input('Income needed at retirement? (percent): ')
	yearsRetirement = input('Expected years of retirement?: ')
	
	yearstoSave = int(ageRetirement) - int(currentAge)
	savedEachyear = int(houseIncome) * float(annualSavingsrate)
	moneyRetirement = int(yearstoSave) * int(savedEachyear) + int(currentSavings)
	
	print('You will have ' + '$' + str(moneyRetirement) + ' saved when you retire')

main()