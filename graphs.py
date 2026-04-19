import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#histogram of salary summary stats
def salaryDistributionHistogram(df, salary_column='normalized_salary'):
    from analyzeData import computeSummaryStatistics #import computeSummaryStatistics from analyzeData.py
    
    summaryStats = computeSummaryStatistics(df, salary_column)
    #print summary stats in console
    print(f"Mean: {summaryStats['mean']}, Median: {summaryStats['median']}, Std: {summaryStats['std']}, Min: {summaryStats['min']}, Max: {summaryStats['max']}")
    
    salaryData = df[salary_column].dropna() #remove missing values
    salaryData = salaryData[salaryData <=500000] #filter extreme values

    fig,ax =plt.subplots()
    sns.histplot(salaryData,bins=20,kde=False,ax=ax) #use seaborn to make a more attractive histogram 
    ax.axvline(summaryStats['mean'], color='blue',linestyle='--',label=f"Mean: ${summaryStats['mean']:,.0f}") 
    ax.axvline(summaryStats['median'], color='purple',linestyle='--',label=f"Median: ${summaryStats['median']:,.0f}")
    ax.set_title('Distribution of Salaries Across Job Postings')
    ax.set_ylabel('Number of Job Postings')
    ax.set_xlabel('Salary (USD)')
    ax.legend()

    plt.tight_layout()
    plt.show()

#table of salary summary stats
def summaryStatsTable(df, salary_column='normalized_salary'):
    from analyzeData import computeSummaryStatistics #import computeSummaryStatistics from analyzeData.py
    
    summaryStats = computeSummaryStatistics(df, salary_column)
    
    #set rows table rows with formatted values
    rows = [
        ("Mean Salary",f"${summaryStats['mean']:,.2f}"),
        ("Median Salary",f"${summaryStats['median']:,.2f}"),
        ("Min Salary",f"${summaryStats['min']:,.2f}"),
        ("Max Salary",f"${summaryStats['max']:,.2f}"),]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.axis('off') #hide axes
    table = ax.table(cellText=rows,colLabels=["Statistic", "Value"],loc='center',cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.3, 1.8) 
    ax.set_title('Salary Summary Statistics', fontsize=13, pad=12)

    plt.show()

#import data and clean data before creating graphs
from loadData import load_csv
from cleanData import clean_data

#test- run graphs.py to see the graphs and summary stats table with the cleaned data from postings.csv
#can remove below code and call graph functions in main.py once done

#load and clean data
filepath = "postings.csv"
df = load_csv(filepath)
df = clean_data(df)

#call methods to create graphs
salaryDistributionHistogram(df)
summaryStatsTable(df)