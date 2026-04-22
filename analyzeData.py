import pandas as pd
import matplotlib.pyplot as plt


def computeSummaryStatistics(df, salary='normalized_salary'):
    mean= df[salary].mean()
    median= df[salary].median()
    std= df[salary].std()
    min= df[salary].min()
    max= df[salary].max()
    return {"mean": mean,"median": median,"std": std,"min": min,"max": max}

#counts jobs by skill
def skillFrequency(df, skill_column='description'):

    #make list of common skills
    skills= ["python", "excel", "communication", "java", "sql", "project management", 
            "data analysis", "critical thinking", "problem solving", "C++", "C#" ,"tableau",
            "power bi", "machine learning", "azure", "cloud", "leadership", "teamwork"]
    
    descriptions= df[skill_column].dropna() #remove values with no description

    skillCount={}

    #add to dict on how many times a skill is in a description
    for skill in skills:
        count=descriptions.str.contains(skill, case=False).sum() #add to count how many descrptions have the skill
        skillCount[skill]= count

    #use df to create table and then sort by count
    value=pd.DataFrame(skillCount.items(),columns=["Skill","Count"]).sort_values("Count",ascending=False) #sort by count

    return value

#counts jobs by work type
def jobsByWorkType(df, workTypeCol='formatted_work_type'):
    workTypeCounts= df[workTypeCol].value_counts().reset_index()
    workTypeCounts.columns= ["Work Type", "Count"]
    return workTypeCounts