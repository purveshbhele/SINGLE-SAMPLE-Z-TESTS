import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import random

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

mean=statistics.mean(data)
std_dev=statistics.stdev(data)

"""print("Mean is",str(mean))
print("Std_dev is",str(std_dev))

fig=ff.create_distplot([data],["Claps"],show_hist=False)
fig.show()"""


def randomSetOfMean(counter):
        dataset=[]
        for i in range(0,counter):
                random_index=random.randint(0,len(data)-1)
                value=data[random_index]
                dataset.append(value)
        mean=statistics.mean(dataset)
        return mean


def show_fig(mean_list):
        df=mean_list
        fig=ff.create_distplot([df],["Claps"],show_hist=False)
        fig.show()


def setUp():
        mean_list=[]
        for i in range(0,1000):
                setOfMeans=randomSetOfMean(100)
                mean_list.append(setOfMeans)
        show_fig(mean_list)
        sampleMean=statistics.mean(mean_list)
        samplestd_dev=statistics.stdev(mean_list)
        print("Mean of sampling distribution is",str(sampleMean))
        print("Std_Dev of sampling distribution is",str(std_dev))
        first_Std_Dev_Start,first_std_Dev_end=sampleMean-samplestd_dev,sampleMean+samplestd_dev
        second_Std_Dev_Start,second_std_Dev_end=sampleMean-(2*samplestd_dev),sampleMean+(2*samplestd_dev)
        third_Std_Dev_Start,third_std_Dev_end=sampleMean-(3*samplestd_dev),sampleMean+(3*samplestd_dev)

        print("std1",first_Std_Dev_Start,first_std_Dev_end)
        print("std2",second_Std_Dev_Start,second_std_Dev_end)
        print("std3",third_Std_Dev_Start,third_std_Dev_end)

        zScore=(sampleMean-mean)/std_dev
        print("Zscore is -",str(zScore))
setUp()