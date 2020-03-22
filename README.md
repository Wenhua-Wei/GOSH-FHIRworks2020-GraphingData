**Graphing_FHIR_Data**

Display the changes of vital signs of patients over time using graphs.

**Setup**

1. For Mac/Linux user, open a new terminal

   For Windows user, open a new Bash terminal (Install Git Bash: https://gitforwindows.org)

1. In the terminal, Clone the repository

        git clone https://github.com/Wenhua-Wei/GOSH-FHIRworks2020-GraphingData.git
2. Use cd command to go to the GOSH-FHIRworks2020-GraphingData directory

3. Activate virtual environment

        source venv/bin/activate
5. Firstly, run the FHIR API repository and open the local host port

        https://github.com/goshdrive/FHIRworks_2020
6. Go back to the GOSH-FHIRworks2020-GraphingData repository, and run the following command

        python app.py
7. Open the local host port 

        http://localhost:8080/
   (If you get an error related to localhost port, please change to another avaliable port on line 106 of app.py)
8. Input a patient ID and select one vital sign to display, then click show to see the graph

**Description**

1. This web app is built with flask framework to display the changes of vital signs of patients over time using graphs done by Chart.js.
    Patients obervation results are obtianed from FHIR API using python.

2. This can be used to futher display other patient data graphically, since patient information has been put to frontend.

