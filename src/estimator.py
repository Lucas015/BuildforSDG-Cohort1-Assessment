import json
import math
import numpy as np

with open("BuildforSDG-Cohort1-Assessment\\src\\data.json","r") as read_file:
  data = json.load(read_file)

def estimator(data):
      
  impact_data = impact(data)
  severeImpact_data = servereImpact(data)

  output_data = {
    "data": data,
    "impact": impact_data,
    "severeImpact": severeImpact_data
  }
  
  return output_data

def impact(data):
      
  currentlyInfected = data['reportedCases'] * 10
  if data['periodType'] == 'days':
       infectionsByRequestedTime = math.pow(2, (data['timeToElapse'] / 3)) * currentlyInfected
  severeCasesByRequestedTime = infectionsByRequestedTime * 0.15
  hospitalBedsByRequestedTime = data['totalHospitalBeds'] - severeCasesByRequestedTime
  casesForICUByRequestedTime = infectionsByRequestedTime * 0.5
  casesForVentilatorsByRequestedTime = infectionsByRequestedTime * 0.2
  dollarsInFlight = (infectionsByRequestedTime * 0.85) * data['region']['avgDailyIncomeInUSD'] * 30

  return json.dumps({
    "currentlyInfected" : currentlyInfected,
    "infectionsByRequestedTime" : math.trunc(infectionsByRequestedTime),
    "severeCasesByRequestedTime" : math.trunc(severeCasesByRequestedTime),
    "hospitalBedsByRequestedTime" : math.trunc(hospitalBedsByRequestedTime),
    "casesForICUByRequestedTime" : math.trunc(casesForICUByRequestedTime),
    "casesForVentilatorsByRequestedTime" : math.trunc(casesForVentilatorsByRequestedTime),
    "dollarsInFlight" : math.trunc(dollarsInFlight)
  })

def servereImpact(data):
  
  currentlyInfected = data['reportedCases'] * 50
  if data['periodType'] == 'days':
       infectionsByRequestedTime = math.pow(2, (data['timeToElapse'] / 3)) * currentlyInfected
  severeCasesByRequestedTime = infectionsByRequestedTime * 0.15
  hospitalBedsByRequestedTime = data['totalHospitalBeds'] - severeCasesByRequestedTime
  casesForICUByRequestedTime = infectionsByRequestedTime * 0.5
  casesForVentilatorsByRequestedTime = infectionsByRequestedTime * 0.2
  dollarsInFlight = (infectionsByRequestedTime * 0.85) * data['region']['avgDailyIncomeInUSD'] * 30

  return json.dumps({
    "currentlyInfected" : currentlyInfected,
    "infectionsByRequestedTime" : math.trunc(infectionsByRequestedTime),
    "severeCasesByRequestedTime" : math.trunc(severeCasesByRequestedTime),
    "hospitalBedsByRequestedTime" : math.trunc(hospitalBedsByRequestedTime),
    "casesForICUByRequestedTime" : math.trunc(casesForICUByRequestedTime),
    "casesForVentilatorsByRequestedTime" : math.trunc(casesForVentilatorsByRequestedTime),
    "dollarsInFlight" : math.trunc(dollarsInFlight)
  })

estimator(data)