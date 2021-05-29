#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 08:46:22 2020

@author: bharat
"""

# Importing the libraries
import pandas as pd
import pickle

#Loading data from CSV Files to Data Frame
AUD_USD = pd.read_csv("DATA/AUD_USD_Final.csv")
EUR_USD = pd.read_csv("DATA/EUR_USD_Final.csv")
GBP_USD = pd.read_csv("DATA/GBP_USD_Final.csv")
USD_CAD = pd.read_csv("DATA/USD_CAD_Final.csv")
USD_JPY = pd.read_csv("DATA/USD_JPY_Final.csv")
Broker_Info = pd.read_csv("DATA/Broker_Info.csv")

AUD_USD.Date = pd.to_datetime(AUD_USD.Date)
EUR_USD.Date = pd.to_datetime(EUR_USD.Date)
GBP_USD.Date = pd.to_datetime(GBP_USD.Date)
USD_CAD.Date = pd.to_datetime(USD_CAD.Date)
USD_JPY.Date = pd.to_datetime(USD_JPY.Date)

pickle.dump([AUD_USD,EUR_USD,GBP_USD,USD_CAD,USD_JPY,Broker_Info], open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
#print(model)