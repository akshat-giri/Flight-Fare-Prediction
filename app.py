# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:06:27 2021

@author: AKSHAT
"""
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

app = Flask(__name__)
Swagger(app)

@app.route("/")
def home():
    return 'Welcome All'
@app.route('/ans')
def predict_price():
    
    """flight Fare Predictor
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Journey day
        in: query
        type: number
        required: true
      - name: Journey month
        in: query
        type: number
        required: true
      - name: Departure hour
        in: query
        type: number
        required: true
      - name: Departure minute
        in: query
        type: number
        required: true
      - name: Departure(PM or AM)
        in: query
        type: string
        required: true
      - name: Arrival day
        in: query
        type: number
        required: true
      - name: Arrival hour
        in: query
        type: number
        required: true
      - name: Arrival minute
        in: query
        type: number
        required: true
      - name: Arrival(PM or AM)
        in: query
        type: string
        required: true
      - name: Airline
        in: query
        type: string
        required: true
      - name: Source
        in: query
        type: string
        required: true
      - name: Destination
        in: query
        type: string
        required: true
      - name: dur_hour
        in: query
        type: number
        required: true
      - name: dur_min
        in: query
        type: number
        required: true
      - name: Total_stops
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    Journey_day=request.args.get("Journey day")
    Journey_month=request.args.get("Journey month")
    Departure_hour=request.args.get("Departure hour")
    Departure_minute=request.args.get("Departure minute")
    Departure_PM_or_Am=request.args.get("Departure_PM_or_Am")
    Arrival_day=request.args.get("Arrival hour")
    Arrival_hour=request.args.get("Arrival hour")
    Arrival_minute=request.args.get("Arrival minute")
    Arrival_PM_or_AM=request.args.get("Arrival_PM_or_AM")
    Airline=request.args.get("Airline")
    Source=request.args.get("Source")
    Destination=request.args.get("Destination")
    dur_hour=request.args.get("dur_hour")
    dur_min=request.args.get("dur_min")
    Total_stops=request.args.get("Total_stops")
    
    
    if(Airline=='Jet Airways'):
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

    elif (Airline=='IndiGo'):
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

    elif (Airline=='Air India'):
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
            
    elif (Airline=='Multiple carriers'):
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
            
    elif (Airline=='SpiceJet'):
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
            
    elif (Airline=='Vistara'):
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

    elif (Airline=='GoAir'):
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

    elif (Airline=='Multiple carriers Premium economy'):
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

    elif (Airline=='Jet Airways Business'):
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

    elif (Airline=='Vistara Premium economy'):
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
            
    elif (Airline=='Trujet'):
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
    
    # Source
    # Banglore = 0 (not in column)
    if (Source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
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

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
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

    elif (Source == 'New_Delhi'):
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

    
    
    
    
    
    prediction=model.predict([[
        Total_stops,
        Journey_day,
        Journey_month,
        Departure_hour,
        Departure_minute,
        Arrival_hour,
        Arrival_minute,
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
        d_New_Delhi]])
    
    
    output=round(prediction[0],2)
    return "The input parameter predicted that the Note is "+ str(output)









if __name__ == "__main__":
    app.run(debug=True)