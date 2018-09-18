#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:23:00 2018

@author: dhruvsubramaniam
INF 559 HW 3 Python Script 
"""
# =============================================================================
import json
import numpy
import os
import re
dirpath = os.getcwd()
#Set Current Working Directory
#os.chdir('/Users/dhruvsubramaniam/Desktop/INF 559/hw3')

# =============================================================================

file = open('lax.json') #Open File
fulldata = json.load(file) # Loading Json Dictionary 
meta = fulldata['meta']
data= fulldata['data']



### List of Unique Terminal, Year abd Traffic Type
terminal_list = []
unique_date = []
unique_trtype = []
for i in data:
    if i[9][0:4] not in unique_date:
        unique_date.append(i[9][0:4])
    if i[10] not in terminal_list:
        terminal_list.append(i[10])
    if i[11] not in unique_trtype:
        unique_trtype.append(i[11])
        
# =============================================================================
#Dictionary and Acronym Creation 
acronym = []
for i in terminal_list:
    acronym.append(''.join(k[0] for k in i.upper().split()))
Dict_Term = dict(zip(acronym,terminal_list))
### Changing the key for Tom Bradley from TBIT to TBI
Dict_Term.pop('TBIT')
Dict_Term['Tbi'] = 'Tom Bradley International Terminal'

# =============================================================================
# =============================================================================
# =============================================================================
#
## USing  Functions 
# For Terminal 
def term(inp,data,Dict_Term):
    count = 0
    data_terminal = []
    for i in data:
        for j in i:
            if (j == Dict_Term[inp]):
                data_terminal.append(i)
                count = count+1
    return(data_terminal)
    
# For Traffic Type  
def traff(inp,data,unique_trtype):
    count2 = 0
    data_traffic = []
    for i in data:
        for j in i:
            if (j == inp):
                data_traffic.append(i)
                count2 = count2+1
    return(data_traffic)
    
    
# For Year
def date(inp,data,unique_date):
    count3 = 0
    data_year = []
    for i in data:
        if (i[9][0:4] == inp):
            data_year.append(i)
            count3 = count3+1
    return(data_year)
    
def passengercount(data):
    count = 0
    passengers = []
    for i in data:
        passengers.append(i[13])
        count = count+1
    passengers = list(map(int, passengers))
    noofpass = sum(passengers) # Number of passengers   
    return(noofpass)
    

# =============================================================================
user_input = input('Input query for Required data:').lower().split()
user_index = []
for i in user_input:
    user_index.append(i.capitalize())
    
# =============================================================================
# =============================================================================
no_of_pass = []
a = []
b = []
c=[]
## Test to see the content of the user_input
for i in user_index:
    a.append(i in Dict_Term)
    b.append(i in unique_trtype)
    c.append(i in unique_date)
aa = True in a
bb = True in b
cc = True in c

if (aa==True):
    no_of_pass = []
    for i in user_index:
        if i in Dict_Term:
            abd = term(i,data,Dict_Term)
            no_of_pass.append(passengercount(abd))
            if (bb==True):
                no_of_pass = []
                if (cc==True):
                    for j in user_index:
                        if (j in unique_trtype):
                            pal = traff(j,abd,unique_trtype)
                            for  k in user_index:
                                if (k in unique_date):
                                    fin = date(k,pal,unique_date)
                                    no_of_pass.append(passengercount(fin))
                elif (cc == False):
            #abd = term(i,data,Dict_Term)
                    for j in user_index:
                        if (j in unique_trtype):
                            pal = traff(j,abd,unique_trtype)
                            no_of_pass.append(passengercount(pal))
        else:
                no_of_pass = []
                for i in user_index:
                    if i in Dict_Term:
                        abd = term(i,data,Dict_Term)
                        if (cc==True):
                            for j in user_index:
                                if (j in unique_date):
                                    fin = date(j,abd,unique_date)
                                    no_of_pass.append(passengercount(fin))
                        elif (cc == False):
            #abd = term(i,data,Dict_Term)
                            no_of_pass.append(passengercount(abd))
else:
    if (bb==True):
        no_of_pass = []
        if (cc==True):
            for j in user_index:
                if (j in unique_trtype):
                    pal = traff(j,data,unique_trtype)
                    for  k in user_index:
                        if (k in unique_date):
                            fin = date(k,pal,unique_date)
                            no_of_pass.append(passengercount(fin))
        else:
            no_of_pass = []
            for j in user_index:
                fpal = traff(j,data,unique_trtype)
                no_of_pass.append(passengercount(fpal))
    else:
        no_of_pass = []
        if (cc==True):
            for j in user_index:
                fpal = date(j,data,unique_date)
                no_of_pass.append(passengercount(fpal))

##Output for Final Number                
print(no_of_pass)
                
                
      
# =============================================================================

        
        
