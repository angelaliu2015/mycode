#!/usr/bin/env python3
import csv
import numpy as np
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list. [0] is LAN and [1] WAN data"""
    summary = [] # list that will contain [(LAN), (WAN)]

    # open csv data
    with open("/home/student/mycode/graphing/2018summary.csv",\
     "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (row[0], row[1], row[2], row[3])
            summary.append(rowdat) # add dict to list
    return summary

def main():
    N = 4
    summary = parsecsvdata()
    localnetMeans = summary[0]
    wanMeans = summary[1]

    ind = np.arange(N)
    width = 0.35
    p1 =plt.bar(ind,localnetMeans,width)
    p2 =plt.bar(ind,wanMeans,width, bottom=localnetMeans)

    plt.ylabel("Lenth of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind,("Q1","Q2","Q3","Q4"))
    plt.yticks(np.arange(0,81,10))
    plt.legend((p1[0],p2[0]),("LAN","WAN"))
    
    plt.savefig\
            ("/home/student/mycode/graphing/2018summary.png")
    print("Graph created")
main()
