# Vityarthi-Project
================================================================================

PROJECT TITLE: PATIENT MEDICAL TEST ANALYZER

OVERVIEW OF THE PROJECT

This project is a Python-based Command Line Interface (CLI) tool designed to
interpret medical laboratory test results. It acts as a digital assistant that
compares patient test values against standard medical reference ranges. Based
on the patient's age and gender, the system analyzes input data to determine
if the results fall within a normal, lower, or higher range.

FEATURES

  Patient Profiling: Accepts and processes Name, ID, Gender, and Age.

  Demographic Logic: Applies specific reference range logic for:

  Adolescents (12 to <18 years old)

  Adults (18+ years old)

  Males and Females

  Instant Analysis: Immediately categorizes test results as Normal, Low, or High.

TECHNOLOGIES/TOOLS USED

  Programming Language: Python 3.x

  Interface: Command Line Interface (CLI) / Terminal

  Libraries: Python Standard Library (No external dependencies required)

  Editor: Compatible with any text or code editor.

STEPS TO INSTALL & RUN THE PROJECT

  Prerequisites: Ensure you have Python 3.x installed.
  (Check by typing 'python --version' in your terminal).

  Download: Save the source code to a file named 'health_check.py'.

  Open Terminal: Navigate to the folder where you saved the file.

  Run Command: Execute the script using the following command:

  python health_check.py

INSTRUCTIONS FOR TESTING

  To verify that the project is working correctly, follow this testing procedure:

  Launch the Application: Run the script in your terminal.

  Input Demographics: Enter Name, ID, Gender ('M' or 'F'), and Age (e.g., 45).

  Select a Test: Choose a specific Code from the table below (e.g., 'GLU').
  
  Input Value: Enter a numerical test result value.
  
  Verify Result: The program will output whether the value is NORMAL, LOWER,
  or HIGHER.

[Test Case Example]
Input:

  Name: Jane Doe
  
  Gender: F
  
  Age: 30
  
  Test: GLU
  
  Value: 85

Expected Output:
  "Your GLUCOSE value is within the NORMAL range."

SUPPORTED TESTS & CODES REFERENCE

  Use these exact codes when prompted to "Enter the test":

    Test Name                   Input Code
    
    Albumin                     ALB
    Ammonia                     NH3
    Bilirubin Conjugated        BILC
    Bilirubin Unconjugated      BILUC
    Amylase                     AMYL
    Calcium                     CAL
    Cholesterol                 CHOL
    Carbon Dioxide              CO2
    Creatine Kinase             CK
    Glucose                     GLU
    Haemoglobin                 HAEM

INPUT REQUIREMENTS

  Gender: Must be entered as capital 'M' or 'F'.
  
  Test Codes: Must be entered exactly as shown in the table (case-sensitive).
  
  Age: The script logic currently supports patients aged 12 and older.

