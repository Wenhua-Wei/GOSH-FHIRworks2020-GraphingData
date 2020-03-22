from flask import Flask, render_template, request, redirect
import os
from test import renderData, patient_info


app = Flask(__name__)

identifier = None


@app.route("/handler", methods=['POST'])
def handle():
    name = request.form["sel1"]
    global identifier
    identifier = request.form["inputID"]
    
    if name == "Respiratory Rate":
        return redirect("/Respiratory_rate")
    elif name == "Body Mass Index":
        return redirect("/Body_Mass_Index")
    elif name == "Body Height":
        return redirect("/Body_Height")
    elif name == "Diastolic Blood Pressure":
        return redirect("/Diastolic_Blood_Pressure")
    elif name == "Systolic Blood Pressure":
        return redirect("/Systolic_Blood_Pressure")
    elif name == "Heart Rate":
        return redirect("/Heart_Rate")
    elif name == "Body Weight":
        return redirect("/Body_Weight")
 
@app.route("/")
def index():
    info = patient_info(identifier)
    # info = patient_info("8f789d0b-3145-4cf2-8504-13159edaa747")

    return render_template("index.html", info = [info], id = ["Input_ID"], unit = [None], label = ["Respiratory Rate", "Body Mass Index", "Body Height", "Diastolic Blood Pressure", "Systolic Blood Pressure", "Heart Rate", "Body Weight"])

@app.route("/Respiratory_rate")
def respiratoryRateData():
    data = renderData(identifier, "Respiratory rate")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]

    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, data = [data], unit = unit[0], info = [info], id = [identifier], label = ["Respiratory Rate", "Body Mass Index", "Body Height", "Diastolic Blood Pressure", "Systolic Blood Pressure", "Heart Rate", "Body Weight"])

    
@app.route("/Body_Mass_Index")
def BodyMassIndexData():
    data = renderData(identifier, "Body Mass Index")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]
    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, unit = unit[0], info = [info], data = [data], id = [identifier], label = ["Body Mass Index", "Respiratory Rate","Body Height", "Diastolic Blood Pressure", "Systolic Blood Pressure", "Heart Rate", "Body Weight"])

@app.route("/Body_Height")
def BodyHeightData():
    data = renderData(identifier, "Body Height")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]
    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, unit = unit[0], info = [info], data = [data], id = [identifier], label = ["Body Height", "Respiratory Rate", "Body Mass Index", "Diastolic Blood Pressure", "Systolic Blood Pressure", "Heart Rate", "Body Weight"])

@app.route("/Diastolic_Blood_Pressure")
def DiastolicBloodPressureData():
    data = renderData(identifier, "Diastolic Blood Pressure")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]
    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, unit = unit[0],info = [info], data = [data], id = [identifier], label = ["Diastolic Blood Pressure", "Respiratory Rate", "Body Mass Index", "Body Height", "Diastolic Blood Pressure", "Systolic Blood Pressure", "Heart Rate", "Body Weight"])

@app.route("/Systolic_Blood_Pressure")
def SystolicBloodPressureData():
    data = renderData(identifier, "Systolic Blood Pressure")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]
    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, unit = unit[0], info = [info], data = [data], id = [identifier], label = ["Systolic Blood Pressure", "Respiratory Rate", "Body Mass Index", "Body Height", "Diastolic Blood Pressure",  "Heart Rate", "Body Weight"])

@app.route("/Heart_Rate")
def HeartRateData():
    data = renderData(identifier, "Heart rate")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]
    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, unit = unit[0], info = [info], data = [data], id = [identifier], label = ["Heart Rate", "Respiratory Rate", "Body Mass Index", "Body Height", "Diastolic Blood Pressure", "Systolic Blood Pressure","Body Weight"])

@app.route("/Body_Weight")
def BodyWeightData():
    data = renderData(identifier, "Body Weight")
    info = patient_info(identifier)
    x_axis = [k for k in data.keys()]
    y_axis = [float(v.split()[0]) for v in data.values()]
    unit = [v.split()[1] for v in data.values()]
    return render_template("index.html", y_axis = y_axis, x_axis = x_axis, unit = unit[0], info = [info], data = [data], id = [identifier], label = ["Body Weight", "Respiratory Rate", "Body Mass Index", "Body Height", "Diastolic Blood Pressure", "Systolic Blood Pressure", "Heart Rate"])

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv('IP', 'localhost'), 
            port=int(os.getenv('PORT', 8080)))
