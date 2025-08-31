from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained pipeline
model = joblib.load("final_student_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect input values from form
        age = int(request.form['age'])
        gender = request.form['gender']
        study_hours = float(request.form['study_hours'])
        social_media = float(request.form['social_media'])
        netflix = float(request.form['netflix'])
        part_time_job = request.form['part_time_job']
        attendance = float(request.form['attendance'])
        sleep_hours = float(request.form['sleep_hours'])
        diet_quality = request.form['diet_quality']
        exercise_freq = int(request.form['exercise_freq'])
        parental_edu = request.form['parental_edu']
        internet_quality = request.form['internet_quality']
        mental_health = int(request.form['mental_health'])
        extracurricular = request.form['extracurricular']

       
        input_data = pd.DataFrame([{
            'age': age,
            'gender': gender,
            'study_hours_per_day': study_hours,
            'social_media_hours': social_media,
            'netflix_hours': netflix,
            'part_time_job': part_time_job,
            'attendance_percentage': attendance,
            'sleep_hours': sleep_hours,
            'diet_quality': diet_quality,
            'exercise_frequency': exercise_freq,
            'parental_education_level': parental_edu,
            'internet_quality': internet_quality,
            'mental_health_rating': mental_health,
            'extracurricular_participation': extracurricular
        }])

        # Predict
        prediction = model.predict(input_data)[0]
        score = round(np.clip(prediction, 0, 100), 2) 
        

        if score >= 90:
            message = " Excellent work! Keep it up!"
        elif score >= 80:
            message = " Great job! You're doing really well!"
        elif score >= 70:
            message = " Good effort! Keep improving."
        elif score >= 60:
            message = " You’re on the right track, just push a bit more!"
        elif score >= 50:
            message = " Don’t give up! Focus more and you’ll improve."
        else:
            message = " Stay strong! Work harder and success will come."

        return render_template('result.html', score=score, message=message)

if __name__ == '__main__':
    app.run(debug=True)
