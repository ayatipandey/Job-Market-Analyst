import pandas as pd
import matplotlib.pyplot as plt


def computeSummaryStatistics(df, salary='normalized_salary'):
    mean= df[salary].mean()
    median = df[salary].median()
    std = df[salary].std()
    min= df[salary].min()
    max = df[salary].max()
    return {"mean": mean, "median": median, "std": std, "min": min, "max": max}
