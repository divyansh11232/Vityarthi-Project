Project Statement: Patient Medical Test Analyzer

1. Problem Statement

In the modern healthcare landscape, patients often receive laboratory test results containing raw numerical data without immediate context. Understanding whether a value like "Glucose: 105 mg/dL" or "Albumin: 4.0 g/dL" is healthy can be difficult for a layperson, as "normal" ranges often fluctuate based on specific demographic factors like age and biological sex. Without professional interpretation, this ambiguity can lead to unnecessary anxiety or a lack of urgency when medical attention is actually required. This project aims to bridge that knowledge gap by providing a quick, automated interpretation of common medical test results.

2. Scope of the Project

The Patient Medical Test Analyzer is designed as a lightweight, logic-based diagnostic aid.

In Scope:

Input Processing: collecting essential patient demographics (Name, Age, Gender) to determine the correct reference dataset.

Test Coverage: Supporting a predefined list of 11 critical laboratory tests, including Glucose, Cholesterol, Haemoglobin, and Bilirubin.

Logic Engine: Comparing user input against standard medical reference intervals for Adolescents (12-18) and Adults (18+).

Output Generation: Delivering immediate textual feedback indicating if results are "Normal," "Lower," or "Higher" than standard limits.

Out of Scope:

Persistent database storage of patient medical history.

Integration with hospital Electronic Health Record (EHR) systems.

Diagnosis of specific diseases or prescription of medication.

Support for patients under the age of 12 (Pediatrics).

3. Target Users

Patients & Individuals: People who have received lab reports and wish to quickly verify where their numbers fall on the spectrum of health before visiting a doctor.

Medical Students & Nursing Students: Learners who need a tool to practice memorizing or verifying reference ranges for different demographics.

Health Enthusiasts: Individuals proactively tracking specific biomarkers (like Glucose or Cholesterol) who need a quick reference tool.

4. High-Level Features

Demographic-Aware Analysis: The system does not use a "one size fits all" approach; it dynamically adjusts the normal reference ranges based on the user's input age and gender.

Test Code System: Implements a streamlined shorthand code system (e.g., GLU, CK, ALB) to speed up data entry and reduce typing errors.

Instant Classification: Provides real-time feedback, classifying numerical inputs into three distinct categories: Normal Range, Low Alert, or High Alert.

CLI Interaction: A simple, text-based interface that requires no complex installation or graphical environment, making it accessible on any machine with Python installed.
