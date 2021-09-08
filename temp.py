import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics 
import random 
import pandas as pd 
import csv 


df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

print(std_deviation)
print(population_mean)

fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="Mean"))
fig.show()

