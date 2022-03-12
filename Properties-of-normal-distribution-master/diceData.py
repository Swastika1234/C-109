import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
diceResult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
mean=sum(diceResult)/len(diceResult)
stdD=statistics.stdev(diceResult)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)


firstStdStart,firstStdEnd=mean-stdD,mean+stdD
secondStdStart,secondStdEnd=mean-(2*stdD),mean+(2*stdD)
thirdStdStart,thirdStdEnd=mean-(3*stdD),mean+(3*stdD)


fig=ff.create_distplot([diceResult],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[firstStdStart,firstStdStart],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[secondStdStart,secondStdStart],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[thirdStdStart,thirdStdStart],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[firstStdEnd,firstStdEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[secondStdEnd,secondStdEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[thirdStdEnd,thirdStdEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3"))


print("mean of the data=    ",mean)
print("median of the data=    ",median)
print("mode of the data=    ",mode)
print("stdD of the data=    ",stdD)