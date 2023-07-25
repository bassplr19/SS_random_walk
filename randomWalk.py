# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:45:17 2023

@author: josh_zagorski
"""
import numpy as np
import pandas as pd
import random
import yfinance as yf
import pyinputplus as pyip

class RandomWalkSimulator:
    def __init__(self,initialValue,timeSpan,changeRange,annualContribution):
        self.initialValue = initialValue
        self.timeSpan = timeSpan
        self.changeRange = changeRange
        self.annualContribution = annualContribution
    
    def randomWalk(self):
        year = []
        yearEndValue = [] 
        currentValue = self.initialValue
        for i in range(0,len(self.timeSpan)-1):
            year.append(int(self.timeSpan[i]))
            yearEndValue.append(round(currentValue,2))
            change = random.choice(self.changeRange)/100*currentValue
            currentValue += self.annualContribution[i] + change
            if currentValue < 0:
                currentValue = 0
        return [year, yearEndValue]
    
    def runRandomWalkMany(self, iterations):
        outputs = []
        for i in range(iterations):
            output = self.randomWalk()
            if i == 0:
                outputs = output
            else:
                outputs.append(output[1])
        outputs = pd.DataFrame(outputs).transpose()
        outputs.set_index(outputs.columns[0], inplace = True)
        outputs.index.name = "Year"
        return outputs
    
def spreturns():
    # Read in S&P 500 Historical Returns
    # Get the S&P 500 closing prices from Yahoo Finance
    sp500 = yf.Ticker("^GSPC").history(start="1928-01-01", end=None)

    # Calculate the daily returns
    sp500["daily_return"] = sp500["Close"].pct_change()

    # Calculate the annual returns
    annual_returns = sp500["daily_return"].resample("Y").apply(lambda x: (1+x).prod() - 1)

    # Calculate the percentage returns
    annual_returns_percentage = annual_returns * 100

    # Create a list of the percentage returns
    return list(annual_returns_percentage)
      
def statsOut(results):       
    results.plot(legend=False)
    stats = pd.DataFrame({
        "Mean": results.mean(axis=1),
        "Median": results.median(axis=1),
        "+Std Dev": results.mean(axis=1) + results.std(axis=1),
        "-Std Dev": results.mean(axis=1) - results.std(axis=1)
    })
    stats.index.name = "Year"
    stats.plot()
    print(f"Mean {int(stats['Mean'].iloc[-1])}")
    print(f"Median {int(stats['Median'].iloc[-1])}")
    return stats 
     
SP500Change = spreturns()

# Social Security Start dates and monthly check

year62 = int(pyip.inputStr("What year will you turn 62? ",allowRegexes=[r'^\d{3}']))
death = int(pyip.inputStr("What year to plan until? ",allowRegexes=[r'^\d{3}']))
check62 = int(pyip.inputStr("What will your monthly check be at 62? ",allowRegexes=[r'^\d{4}']))
check67 = int(pyip.inputStr("What will your monthly check be at 67? ",allowRegexes=[r'^\d{4}']))
check70 = int(pyip.inputStr("What will your monthly check be at 70? ",allowRegexes=[r'^\d{4}']))
ssStats = [[year62,check62],[year62+5,check67],[year62+8,check70]]

# Test Set
# ssStats = [[2045,2170],[2050,3099],[2053,3848]]
# When do you think you will die?
# death = 2067

numRuns = 200
timeSpanSet = []
annualContributionSet = []
stats = []

for ssSet in ssStats:
    initialValue = 0
    timeSpan = range(ssSet[0],death,1)
    timeSpanSet.append(timeSpan)
    annualContribution = ssSet[1]*12*np.ones([len(timeSpan)])
    annualContributionSet.append(annualContribution)
    simulator = RandomWalkSimulator(initialValue, timeSpan, SP500Change, annualContribution)
    results = simulator.runRandomWalkMany(numRuns)
    stats.append(statsOut(results))
