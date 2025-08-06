from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('credit_model.lb')  # Replace with your trained model

history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'POST':
        age = float(request.form['age'])
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        balance = float(request.form['balance'])
        housing = request.form['housing']
        duration = float(request.form['duration'])
        campaign = float(request.form['campaign'])

        print('output>>>>>>',age, job, marital, education, balance, housing, duration, campaign)
        input_data = [[age, job, marital, education, balance, housing, duration, campaign]]
        prediction = model.predict(input_data)[0]

        history.append((age, job, marital, education, balance, housing, duration, campaign, prediction))

        prediction = model.predict(input_data)[0]
        print("Prediction from model:", prediction)

        return render_template('project.html', prediction=prediction)
    return render_template('project.html')

@app.route('/history')
def show_history():
    return render_template('history.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)