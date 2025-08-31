# Student Performance Predictor

This project predicts student academic performance based on multiple lifestyle, academic, and social factors.  
It uses a Machine Learning model(linear regression) integrated with a Flask web app for easy interaction.

## Features
Takes input such as:
  - Age, Gender
  - Study hours/day, Social media hours/day, Netflix hours
  - Part-time job (Yes/No), Attendance (%), Sleep hours
  - Diet quality (Poor/Fair/Good), Exercise frequency
  - Parental education level (High School/Bachelor/Graduate/None)
  - Internet quality (Good/Poor/Fair)
  - Mental health rating, Extracurricular participation (Yes/No)
Predicts student performance level  
Simple web interface for input and result display

Student_Performance_Predictor/ 
        ├── static/ │
               └── style.css
        ├── templates/ │
              ├── index.html │
              └── result.html
        ├── app.py
        ├── final_student_model.pkl 

## Folder Structure
|- static 
    |- style.css
|- templates
    |- index.html
    |- result.html
|- app.py
|- final_student_model.pkl

## Tech Stack 
Machine Learning: scikit-learn, pickle
Backend: Flask, Python
frontend: HTML, CSS
