**Graphing_FHIR_Data**

This package uses the FHIR standard data, and graphically display the changes of patients' vital signs over time, including Respiratory Rate, Diastolic Blood Pressure, Systolic Blood Pressure, Heart Rate, Body Mass Index, Body Height and Body Height.

**Setup**

**Before setting up the package, follow the link below to run the GOSH Drive and open the local host port:**

   https://github.com/goshdrive/FHIRworks_2020
   
1. For Mac/Linux user, open a new terminal

   For Windows user, open a new Bash terminal (Install Git Bash: https://gitforwindows.org)

2. In the terminal, Clone the repository

        git clone https://github.com/Wenhua-Wei/GOSH-FHIRworks2020-GraphingData.git
        
3. Use cd command to go to the GOSH-FHIRworks2020-GraphingData directory

3. Activate virtual environment

        source venv/bin/activate
        
4. Install libraries (in virtual environment)

        pip install -r requirements.txt
        
5. Go back to the GOSH-FHIRworks2020-GraphingData repository, and run the following command

        python app.py
        
6. If successfully run the package, those message will display in your terminal

        * Serving Flask app "app" (lazy loading)
        * Environment: production
        WARNING: This is a development server. Do not use it in a production deployment.
        Use a production WSGI server instead.
        * Debug mode: on
        * Running on http://localhost:8080/ (Press CTRL+C to quit)
        
6. Open the local host port 

        http://localhost:8080/
       (If you get an error related to localhost port, please change to another avaliable port on line 106 of app.py)
   
   
7. Input a patient ID and select one vital sign to display, then click show to see the graph

**Description**

1. This web app is built with flask framework to display the changes of vital signs of patients over time using graphs done by      
   Chart.js.
   Patients obervation results are obtianed from FHIR API using python.

2. This can be used to futher display other patient data graphically, since patient information has been put to frontend.

