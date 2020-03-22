from typing import List
import datetime

class Extension:
    def __init__(self, url: str, val):
        self.url = url
        self.val = val
    def get_url(self):
        return self.url
    def get_val(self):
        return self.val

class Identifier:
    def __init__(self, system: str, value: str, code: str, display: str, text: str):
        self.system: str = system
        self.value: str = value
        self.code: str = code
        self.display: str = display
        self.text = text

class Address:
    def __init__(self, city: str, state: str, country: str, lines: List[str], latitude: str, longitude: str):
        self.city = city
        self.state = state
        self.country = country
        self.lines = lines
        self.latitude = latitude
        self.longitude = longitude

    def get_address(self):
        street = '\n'.join(self.lines)
        full = street + '\n' + self.city + '\n' + self.state + '\n' + self.country
        return full

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

class Name:
    def __init__(self, given: List[str], family: str, prefix: List[str]):
        self.givenName = given
        self.familyName = family
        self.prefix = prefix

    def get_given(self):
        return ' '.join(self.givenName)
    
    def get_family(self):
        return self.familyName
    
    def get_prefix(self):
        return ' '.join(self.prefix)

    def get_full(self):
        return str(self.get_prefix()) + ' ' + str(self.get_given())+ ' ' + str(self.get_family())

class Telecom:
    def __init__(self, system: str, value: str, use: str):
        self.system = system
        self.value = value
        self.use = use

    def get_system(self):
        return self.system
    
    def get_value(self):
        return self.value

    def get_use(self):
        return self.use

    def get_full(self):
        return self.use + ' ' + self.system + ': ' + self.value

class Communication:
    def __init__(self, language: str, code: str):
        self.language = language
        self.code = code
    def get_language(self):
        return self.language
    def get_code(self):
        return self.code

class Patient:
    def __init__(self, id: str, name: Name, identifier: List[Identifier], 
                extensions: List[Extension], address: Address, telecom: List[Telecom], 
                gender: str, birthdate: str, maritalStatus: str, communication: Communication, multipleBirthBoolean: bool):
        self.id = id
        self.name = name
        self.identifier = identifier
        self.extensions = extensions
        self.address = address
        self.telecom = telecom
        self.gender = gender
        self.birthdate = birthdate
        self.maritalStatus = maritalStatus
        self.communication = communication
        self.multipleBirthBoolean = multipleBirthBoolean
    
    def get_name(self):
        return self.name.get_full()

    def get_address(self):
        return self.address.get_address()
    
    def get_lati(self):
        return self.address.get_latitude()

    def get_longi(self):
        return self.address.get_longitude()

    def get_telecom(self):
        teleList = self.telecom
        if len(teleList) == 1:
            return teleList[0].get_full()

    def get_gender(self):
        return self.gender

    def get_birthdate(self):
        return self.birthdate

    def get_age(self):
        return (datetime.date.today() - self.birthdate).days / 365.25
    
    def get_maritalStatus(self):
        return self.maritalStatus

    def get_communication(self):
        return self.communication.get_code() + ' ' + self.communication.get_language()

    def get_multipleBirthBoolean(self):
        return self.multipleBirthBoolean

    
