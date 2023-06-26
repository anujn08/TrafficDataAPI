from bs4 import BeautifulSoup
import requests 
import pandas as pd
import numpy as np
import schedule
#import datetime
import os
import time
from datetime import datetime, timedelta
# import time
import os
from bs4 import BeautifulSoup
import requests
from xml.etree.ElementTree import XML, fromstring, tostring
import pandas as pd
# %matplotlib inline
from matplotlib import pyplot as plt

path = 'D:\Anuj\Here\Ludhiana_New25_6_23'   

page = requests.get("https://traffic.ls.hereapi.com/traffic/6.2/flow.xml?apiKey=BofRfA3YMcL6BLZnsnQQlQJ-87EJbpKwt3HnxWYnBLs&bbox=30.9146,75.9632;30.8795,75.8640&responseattributes=sh,fc")
soup = BeautifulSoup(page.text, "lxml")
roads = soup.find_all('fi')
#print(soup)
#roads

def get_traffic_data():
    data_dict = {"names":[],"speed":[],"lattitude":[],"Longitude":[],"fc":[],'le':[],'qd':[],'cn':[], 'ff':[], 'jf':[], 'sp':[],'ty':[]}

    #print("LOOP")
    for road in roads:
        myxml = fromstring(str(road))
        fc=5
        for child in myxml:
    #         print(child.tag, child.arrrib)
            if 'de' in child.attrib:
                de=str(child.attrib['de'])
            if 'qd' in child.attrib:
                qd=str(child.attrib['qd'])
            if 'le' in child.attrib:
                le=float(child.attrib['le'])
            if 'fc' in child.attrib:
                fc=int(child.attrib['fc'])
            if 'cn' in child.attrib:
                cn=float(child.attrib['cn'])
            if 'su' in child.attrib:
                su=float(child.attrib['su'])
            if 'ff' in child.attrib:
                ff=float(child.attrib['ff'])
            if 'jf' in child.attrib:
                jf=float(child.attrib['jf'])
            if 'sp' in child.attrib:
                sp=float(child.attrib['sp'])
            if 'ty' in child.attrib:
                ty=child.attrib['ty']
        #if fc <= 4 and cn >=0.7:
        shps = road.find_all('shp')
        #print("IN LOOP ")
        #print(len(shps))
        for j in range(len(shps)): # going through all the shapes in a FI
            coords = shps[j].text.replace(',',' ').split() #list
            las = []
            lons = []
            for i in range(int(len(coords)/2)): # going through all the lat longs in a shp
                las.append(float(coords[2*i]))
                lons.append(float(coords[2*i+1]))
            #loc_pros.append([float(su),float(ff)])
            #data_dict['Road_Name'].append([de])
            data_dict['lattitude'].append(las)
            data_dict['Longitude'].append(lons)
            #lats.append(las)
            #longs.append(lons)
            data_dict['names'].append(de)
            data_dict['speed'].append(float(su))
            data_dict['fc'].append(fc)
            data_dict['le'].append(le)
            data_dict['qd'].append(qd)
            data_dict['cn'].append(cn)
            data_dict['ff'].append(ff)
            data_dict['jf'].append(jf)
            data_dict['sp'].append(sp)
            data_dict['ty'].append(ty)

    df=pd.DataFrame(data_dict)
    return df


def getTime():
    now = datetime.now()
    current_time = now.strftime("%d-%b-%Y-%H-%M")
    return current_time

def realTime_to_schedule():    
    outFile = path + '\\' + getTime() + '.csv'
    data = get_traffic_data()

    if data is None:
        pass
    else:
        print("Writing data to " + outFile)
        data.to_csv(outFile)
        
schedule.every(1).minutes.do(realTime_to_schedule)
# warnings.filterwarnings("ignore")

while True:
    schedule.run_pending()
    time.sleep(1)
