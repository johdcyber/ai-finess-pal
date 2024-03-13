from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gender = request.form['gender']
        current_weight = float(request.form['current_weight'])  # in pounds
        height_feet = int(request.form['height_feet'])  # in feet
        height_inches = int(request.form['height_inches'])  # in inches
        desired_weight = float(request.form['desired_weight'])  # in pounds
        activity_level = request.form['activity_level']

        # Convert height to inches in total, then to cm
        total_height_inches = height_feet * 12 + height_inches
        height_cm = total_height_inches * 2.54

        # Convert weight to kg for the calculation
        weight_kg = current_weight * 0.453592

        # Calculate BMR based on gender
        if gender == 'male':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * 32 + 5  # Example age used, adjust as needed
        else:
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * 32 - 161  # Example age used, adjust as needed

        # Adjust BMR based on activity level
        activity_factors = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extra_active': 1.9
        }
        tdee = bmr * activity_factors[activity_level]

        # Render results with the calculated TDEE
        return render_template('results.html', tdee=tdee, current_weight=current_weight, desired_weight=desired_weight)

    # Render the form if not POST request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
