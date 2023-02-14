# Project 3 ReadMe
<h2> An Analysis of Global Fishing Activity </h2>
<body>
  Welcome to our group's repository for Project 3. The folder Project-3-Final contains the following sub-folders: <br>
  1. Data_Cleaning, which contains:<br>
      &nbsp;&nbsp;• the raw csv files downloaded from the Global Fishing Watch website (voyages_202301.csv.zip, named_anchorages_v2_20221206.csv, fishing-vessels-v2.csv) <br>
      &nbsp;&nbsp;• the Python Jupyter Notebooks used to clean the raw data <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Data_Cleaning_Day2.ipynb contains the code used to create the cleaned csv files (AnchoragesClean.csv, Finalcleanedvoyages.csv, VesselsClean.csv) that were used as the basis for the tables in our SQL database. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Data_Cleaning_ForDash.ipynb contains the code used to create the csv files used in the Dash application. <br>
  <br>
  <br>
  2. Postgres_DB, which contains the database file that we exported following the creation of the database <br>
  <br>
  <br>
  3. Dash_App, which contains the code (app_test.py) and the cleaned csv files used to create the interactive dashboard and visualizations.<br>
  Please run the app_test.py file in your command line to initialize the dashboard. Happy fishing!
