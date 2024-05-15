import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb
from scipy import stats
import scipy
import plotly.offline as pyoff
import plotly.graph_objs as go
from datetime import datetime, date
import matplotlib.ticker as ticker



def univariate_analysis_continuous_variable(df, feature):
    print("Describe:")
    print(feature.describe(include = 'all'))
    print("Mode:", feature.mode())
    print("Range:", feature.values.ptp())
    print("IQR:", scipy.stats.iqr(feature))
    print("Var:", feature.var())
    print("Skew:", feature.skew())
    print("Kurtosis:", feature.kurtosis())


def univariate_visualization_analysis_continuous_variable(df,feature):
    sb.set()
    fig, (ax0, ax1) = plt.subplots(1,2, figsize = (15,5) )  
    sb.distplot(feature, ax= ax0, color= "#005A74")
    sb.boxplot(data= df, x = feature, ax = ax1, color= "#005A74")
    plt.show()

#Number of upper, lower outliers
def check_outlier(df, feature):
    # sb.boxplot(data = df, y = feature)
    # plt.show()
    Q1 = np.percentile(feature, 25)
    Q3 = np.percentile(feature, 75)
    n_O_upper = df[feature > (Q3 + 1.5*scipy.stats.iqr(feature))].shape[0]
    print("Number of upper outliers:", n_O_upper)
    n_L_upper = df[feature < (Q1 - 1.5*scipy.stats.iqr(feature))].shape[0]
    print("Number of lower outliers:", n_L_upper)
    #Percentage of outliers
    outliers_per = round(((n_O_upper + n_L_upper)/df.shape[0])*100,0)
    print("Percentage of outliers:", outliers_per,"%")
    return  n_O_upper, n_L_upper, outliers_per