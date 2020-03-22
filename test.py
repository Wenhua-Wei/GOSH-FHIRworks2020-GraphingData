from fhirParser import patient, fhir, jsonToObj

from fhirParser.fhir import FHIR
from fhirParser.jsonToObj import *
from fhirParser.patient import Patient, Name, Telecom, Address, Communication
import datetime

def sortData(dic):
    sortedData = {}
    sortedVal = {}
    for i in sorted(dic):
        sortedVal.update({i: dic[i]})
    return sortedVal

def formatData(obs: Observation, index: int):
    date = str(obs.get_effectDate()).split(' ')[0]
    value = obs.get_value()[index]
    unit = obs.get_unit()[index]
    val = str(value) + ' ' + unit
    dic = {date: val}
    return dic

def renderData(id: str, displayType: str):
    f = FHIR()
    observarions = f.get_patient_observations(id)
    resp_rate_data_fulldic = {}
    resp_rate_data = {}

    for obs in observarions:
        display = obs.get_display()
        if(display[0] in displayType or displayType in display[0]):
            inx = display.index(displayType)
            dic = formatData(obs, inx)
            resp_rate_data.update(dic)
    resp_rate_data_fulldic.update({displayType: resp_rate_data})
    dic = resp_rate_data_fulldic[displayType]
    
    return sortData(dic)

def patient_info(id: str):
    if id == None:
        return {"id": "Input ID"}
    f = FHIR()
    p = f.get_single_patient(id)
    birth = p.get_birthdate()
    infoDic = {
        "id": id, "Name": p.get_name(), "Gender": p.get_gender(), "BirthDate": birth.strftime('%d/%m/%Y'), "Age": p.get_age(), 
        "Address": p.get_address(), "Accurate location": {"Latitude": p.get_lati(), "Longitude": p.get_longi()}, 
        "Contact": p.get_telecom(), "Language": p.get_communication()
    }
    return infoDic
    
    