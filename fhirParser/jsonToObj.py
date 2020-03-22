from fhirParser.patient import Patient, Name, Address, Extension, Telecom, Communication
from fhirParser.observation import Observation, ValueQuantity
import json
import dateutil.parser

def get_nameObj(nameDic):
    familyName = nameDic["family"]
    givenName = nameDic["given"]
    prefix = nameDic["prefix"]
    return Name(givenName, familyName, prefix)

def extension_val(ext):
    val = ''
    if "valueCoding" in ext:
        val = ext["valueCoding"]
    elif "valueString" in ext:
        val = ext["valueString"]
    elif "valueString" in ext:
        val = ext["valueString"]
    elif 'valueDecimal' in ext:
        val = ext['valueDecimal']
    elif 'valueAddress' in ext:
        val = ', '.join(ext['valueAddress'].values())
    return val

def get_extension(extensionList):
    url = ''
    extensions = []
    for ext in extensionList:
        # url = ext["url"]
        if "extension" in ext:
            for e in ext["extension"]:
                val = extension_val(e)
                url = e["url"]
                extensions.append(Extension(url, val))    
        else:
            val = extension_val(ext)
            url = ext["url"]
            extensions.append(Extension(url, val))
    return extensions

def get_addressObj(addressDic):
    street = addressDic["line"]
    city = addressDic["city"]
    state = addressDic["state"]
    country = addressDic["country"]

    extensions = get_extension(addressDic["extension"])
    print("extensions", extensions[0], extensions[1])
    latitude = ''
    longitude = ''
    for e in extensions:
        if e.get_url() == "latitude":           
            latitude = e.get_val()
        elif e.get_url() == "longitude":
            longitude = e.get_val()

    return Address(city, state, country, street, latitude, longitude)

def get_teleObj(teleList):
    teles = []
    for tele in teleList:
        sys = tele["system"]
        val = tele["value"]
        use = tele["use"]

        telecom = Telecom(sys, val, use)
        teles.append(telecom)
    return teles

def get_communicationObj(communicationDic):
    dic = communicationDic["language"]
    text = dic["text"]
    dic2 = dic["coding"][0]
    code = dic2["code"]

    return Communication(text, code)

def jsonToPatient(input: str):
    data = json.loads(input)
    if data["resourceType"] != "Patient":
        raise AssertionError('Not a patient resource type')
    id = data["id"]

    nameDic = data["name"][0]
    name = get_nameObj(nameDic)

    identifier = data["identifier"]
    extension = data["extension"]
    addressDic = data["address"][0]
    address = get_addressObj(addressDic)

    telecomList = data["telecom"]
    telecoms = get_teleObj(telecomList)

    gender = data["gender"]
    birth = data["birthDate"]
    birth_date: datetime.date = dateutil.parser.isoparse(birth).date()

    maritalStatusDic = data["maritalStatus"] #dic
    maritalStatus = maritalStatusDic["text"]

    communicationDic = data["communication"][0]
    commuObj = get_communicationObj(communicationDic)

    multipleBirthBoolean = data["multipleBirthBoolean"]


    p = Patient(id, name, identifier, extension, address, telecoms, gender, birth_date, maritalStatus, commuObj, multipleBirthBoolean)
    return p

def json_to_valueQuantity(data: str):
    # data = json.loads(input)
    system = data["code"]["coding"][0]["system"]
    code = data["code"]["coding"][0]["code"]
    display = data["code"]["coding"][0]["display"]
    value = None
    unit = None
    if "valueQuantity" in data:
        value = data["valueQuantity"]["value"]
        unit = data["valueQuantity"]['unit']
    return ValueQuantity(value, unit, system, code, display)

def json_to_observation(input: str):
    data = json.loads(input)
    if not data['resourceType'] == 'Observation':
        raise AssertionError('Not an observation resource type')
    id = data["id"]
    status = data["status"]

    pId = data["subject"]["reference"].split('/')[1]
    eId = None
    if "encounter" in data:
        eId = data["encounter"]["reference"].split('/')[1]
    effective_datetime = None
    if "effectiveDateTime" in data:
        effective_datetime = dateutil.parser.isoparse(data['effectiveDateTime'])
    issued_datetime = None
    if "issued" in data:
        issued_datetime = dateutil.parser.isoparse(data['issued'])

    valQuality = []
    if 'code' in data:
        valQuality.append(json_to_valueQuantity(data))

    if 'component' in data:
        for c in data['component']:
            valQuality.append(json_to_valueQuantity(c))
    return Observation(id, status, pId, eId, effective_datetime, issued_datetime, valQuality)

def json_to_observations(input: str):
    input = json.loads(input)

    observations = []
    for i in input:
        if 'entry' in i:
            for p in i['entry']:
                observations.append(json_to_observation(json.dumps(p['resource'])))
    return observations