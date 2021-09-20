 
import streamlit as st
import time
import datetime
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
from datetime import datetime, date, time
image = Image.open('logo.jpg')
st.image(image, '')
model = pickle.load(open("flight_rf.pkl", "rb"))
def team_report():
    #temp_array=list()
    date_dep=st.sidebar.date_input('Departure Date')
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
    #st.subheader("Journey Date : "+str(Journey_day)+str(Journey_month))
    Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
    # print("Departure : ",Dep_hour, Dep_min)

    
    # Arrival
    date_arr = st.sidebar.date_input('Arrival Date')
    Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
     # print("Arrival : ", Arrival_hour, Arrival_min)

     # Duration
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    
    
    Total_stops = int(st.sidebar.selectbox('Select No. of Stops',('0', '1', '2','3','4')))
    
    airline=st.sidebar.selectbox('In which Airline you want to travel?',('Jet Airways', 'IndiGo', 'Air India','Multiple  carriers','SpiceJet','Vistara','GoAir','Multiple carriers Premium economy','Jet Airways Business','Vistara Premium economy','Trujet'))
    if(airline=='Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
        

            
    elif (airline=='Multiple carriers'):

        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
            
    elif (airline=='SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
        
        
            
    elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0 
            
    elif (airline=='Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 




    Source = st.sidebar.selectbox('Source',('Delhi', 'Kolkata', 'Mumbai','Chennai'))
    if (Source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata =1
        s_Mumbai = 0
        s_Chennai = 0
           

    elif (Source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0
            

    elif (Source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1
            

    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0



    
    Source = st.sidebar.selectbox('Destination',('Cochin', 'Delhi', 'New Delhi','Hyderabad','Kolkata'))
    if (Source == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        
    elif (Source == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Source == 'New Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Source == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0

    elif (Source == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0


    temp_array=[[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]]

    return temp_array



team_data = team_report()
st.text("")
st.text("")
st.text("")
submit=st.button('PREDICT FLIGHT PRICE')

if(submit):
    
    score = model.predict(team_data)
    output=round(score[0],2)
    st.subheader('Predicted Price : '+str(output))
            
    



