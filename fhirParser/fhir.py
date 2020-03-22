import requests as req
from urllib.parse import urljoin
from fhirParser.jsonToObj import *
from typing import List

class FHIR:
    def __init__(self, endpoint: str = "https://localhost:5001/api/", verify_ssl: bool = False):
        self.endpoint = endpoint
        self.verify_ssl = verify_ssl
        # from req.packages.urllib3.exceptions import InsecureRequestWarning
        # req.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    def get_single_patient(self, id: str):
        resp = req.get(urljoin(self.endpoint, 'Patient/' + str(id)), verify = self.verify_ssl)
        patientData = resp.text
        patient = jsonToPatient(patientData)
        return patient

    def get_observation(self, id: str):
        response = req.get(urljoin(self.endpoint, 'Observation/single/' + str(id)), verify=self.verify_ssl)
        return json_to_observation(response.text)

    def get_patient_observations(self, id: str):
        response = req.get(urljoin(self.endpoint, 'Observation/' + str(id)),
                                verify=self.verify_ssl)
       
        return json_to_observations(response.text)
        
  