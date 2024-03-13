# Flask Weight Loss Calculator

## Overview

This Flask application provides a simple interface for users to calculate their Total Daily Energy Expenditure (TDEE) based on their current weight, height, gender, and activity level. Users can also input their desired weight to receive recommendations on daily calorie intake to achieve their weight loss goals.

## Features

- User input for gender, current weight, height, desired weight, and activity level.
- Calculation of TDEE based on the Mifflin-St Jeor Equation.
- Recommendations for daily calorie intake for weight loss.

## File Structure

- `app.py`: The main Flask application file. Contains routes and logic for TDEE calculation.
- `requirements.txt`: Lists all the Python packages that the app depends on.
- `Procfile`: Used by DigitalOcean's App Platform (or other PaaS providers) to run the application.
- `templates/`: Directory containing Jinja2 templates for the app.
  - `index.html`: The main page template, displaying the form for user input.
  - `results.html`: Displays the calculated TDEE and recommended calorie intake.
- `static/`: (If applicable) Directory for static files like CSS, JavaScript, and images.

## How It Works

### TDEE Calculation

The application calculates the Total Daily Energy Expenditure (TDEE) using the Mifflin-St Jeor Equation, which requires the user's weight, height, age, and gender. Based on the user's activity level, it then adjusts the TDEE accordingly.

### Calorie Recommendations

Based on the calculated TDEE and the user's weight loss goals, the application suggests a daily calorie intake. It typically recommends a deficit of 500 to 1000 calories per day from the TDEE for healthy weight loss.

## Setup and Deployment

### Local Setup

1. Clone the repository and navigate to the app directory.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
