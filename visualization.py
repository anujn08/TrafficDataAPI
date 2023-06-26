import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

path = 'D:\Anuj\Here\Ludhiana_New25_6_23'   

def getTime():
    now = datetime.now()
    current_time = now.strftime("%d-%b-%Y-%H-%M")
    return current_time

def visualize(path):
    df=pd.read_csv(path)
    fig=plt.figure(figsize=(14,8.0))
    plt.rcParams['axes.facecolor'] = 'white'
    plt.grid(False)

    #print("Lattitude=",len(df["lattitude"]))

    for i in range(len(df["lattitude"])):
        x=df["lattitude"][i].split(',')
        x[0],x[-1]=x[0][1:],x[-1][:-1]

        y=df["Longitude"][i].split(',')
        y[0],y[-1]=y[0][1:],y[-1][:-1]

        lat = [eval(j) for j in x]
        lon = [eval(j) for j in y]

        speed=df["speed"]

        if float(speed[i]) == 0:
            plt.plot(lon,lat,c='gray',linewidth=5)
        elif float(speed[i]) < 10:
            plt.plot(lon,lat,c='brown',linewidth=5)
        elif float(speed[i]) < 15:
            plt.plot(lon,lat,c='orange',linewidth=3)
        elif float(speed[i]) < 20:
            plt.plot(lon,lat,c='yellow',linewidth=2)
        else: # more than 20.
            plt.plot(lon,lat,c='green',linewidth=1)

    plt.axis('on')
    plt.title("SP "+getTime())
    #plt.legend()
    print("Visualized "+path)
#visualize()

for i in os.listdir(path):
    if i.endswith(".csv"):
        print(path+"\\"+i)
        visualize(path+"\\"+i)