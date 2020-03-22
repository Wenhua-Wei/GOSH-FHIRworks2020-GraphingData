import datetime
from typing import List

class ValueQuantity:
    def __init__(self, value, unit: str, system: str, code: str, display: str):
        self.value = value
        self.unit = unit
        self.system = system
        self.code = code
        self.display = display

    def quantity(self) -> str:
        return str(self.value if self.value is not None else 'N/A') + (self.unit if self.unit is not None else '')

    def __str__(self) -> str:
        return self.display + ': ' + str(self.value if self.value is not None else 'N/A') + (self.unit if self.unit is not None else '')


class Observation:
    def __init__(self, id: str, status: str, patientId: str, encounterId: str, 
                 effectiveDatetime: datetime.datetime, issuedDatetime: datetime.datetime,
                 valueQuantity: List[ValueQuantity]):
        self.id = id
        self.status= status
        self.patientId = patientId
        self.encounterId= encounterId
        self.effectiveDatetime= effectiveDatetime
        self.issuedDatetime = issuedDatetime
        self.valueQuantity = valueQuantity
    
    def get_effectDate(self):
        return self.effectiveDatetime
    
    def get_display(self):
        displays = []
        for val in self.valueQuantity:
            displays.append(val.display)
        return displays

    def get_value(self):
        vals = []
        for val in self.valueQuantity:
            vals.append(val.value)
        return vals

    def get_unit(self):
        units = []
        for val in self.valueQuantity:
            units.append(val.unit)
        return units
