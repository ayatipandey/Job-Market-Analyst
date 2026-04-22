import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#histogram of salary summary stats
def salaryDistributionHistogram(df, salary_column='normalized_salary'):
    from analyzeData import computeSummaryStatistics #import computeSummaryStatistics from analyzeData.py
    
    summaryStats = computeSummaryStatistics(df, salary_column)
    
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

    #print summary stats in console
    print(f"Mean: {summaryStats['mean']}, Median: {summaryStats['median']}, Std: {summaryStats['std']}, Min: {summaryStats['min']}, Max: {summaryStats['max']}")

    return fig

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

    return fig

#bar chart of skill frequency using seaborn
def skillFrequencyBarChart(df, skill_column="description", top_n=10):
    
    #retrieve the top n skills and their counts
    skillFreq = skillFrequency(df, skill_column).head(top_n)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=skillFreq,x="Count", y="Skill", ax=ax, palette="rocket_r")
    ax.set_title("Top Skills in Job Descriptions")
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Skill")
    
    plt.tight_layout()
    return fig

#bar chart of jobs by work type using seaborn
def jobByWorkTypeBarChart(df, workTypeCol='formatted_work_type'):
    
    #retrieve counts of each work type (contract, full-time, part-time)
    workTypeCounts = jobsByWorkType(df, workTypeCol)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=workTypeCounts,x="Work Type", y="Count", ax=ax, palette="husl")
    ax.set_title("Jobs by Work Type")
    ax.set_xlabel("Work Type")
    ax.set_ylabel("Number of Job Postings")
    
    plt.tight_layout()
    return fig

#import data and clean data before creating graphs
from loadData import load_csv
from cleanData import clean_data
from analyzeData import skillFrequency, jobsByWorkType

#can be removed once done testing 
# if __name__ == "__main__":
#     filepath = "postings.csv"
#     raw = load_csv(filepath)
#     df = clean_data(raw)

#     fig1 = skillFrequencyBarChart(df)
#     plt.show()

#     fig2 = jobByWorkTypeBarChart(df)
#     plt.show()