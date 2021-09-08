
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics 
import random 
import pandas as pd 
import csv 

df=pd.read_csv("data.csv")
data=df["temp"].tolist()

dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)

std_deviation=statistics.stdev(dataset)

print(mean)
print(std_deviation)