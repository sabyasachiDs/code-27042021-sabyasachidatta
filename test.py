# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:22:55 2021

@author: sabya
"""

import json

#given sample dataset
main=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]
    
#BMI calculation function along with other parameters
def BMI_check(main:list):
    data=main
    elements=len(data)
    res=[]
    for i in range(elements):
        data2=main[i]
        height=main[i]['HeightCm']/100 #in meter
        weight=main[i]['WeightKg']
        bmi=round(weight/height**2,1)
        data2['bmi in kg/m2']=bmi
        if (bmi<=18.4):
            data2['BMI Category']='Underweight'
            data2['Health risk']= 'Malnutrition risk'
            res.append(data2)
        elif (bmi >=18.5 and bmi <= 24.9):
            data2['BMI Category']='Normal weight'
            data2['Health risk']= 'Low risk'
            res.append(data2)
        elif (bmi >=25 and bmi<=29.9):
            data2['BMI Category']='Overweight'
            data2['Health risk']= 'Enhanced risk'
            res.append(data2)
        elif (bmi >=30 and bmi<=34.9):
            data2['BMI Category']='Moderately obese'
            data2['Health risk']= 'Medium risk'
            res.append(data2)
        elif (bmi >=35 and bmi<=39.9):
            data2['BMI Category']='Severely obese'
            data2['Health risk']= 'High risk'
            res.append(data2)
        else:
            data2['BMI Category']='Very severely obese'
            data2['Health risk']= 'Very high risk'
            res.append(data2)
            
    return res

#Overweight counter function
    
def overweight(res:list):
    data=res
    elements=len(data)
    count=0
    for i in range(elements):
        if (res[i]['BMI Category']=='Overweight'):
            count=count+1
            
    return count

#Results
    
result1=BMI_check(main)
print(result1)

result2=overweight(main)
print(result2)