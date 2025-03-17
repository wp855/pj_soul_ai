# Housing Price Prediction - Flask App

This is a Machine Learning Flask web application that predicts house prices based on user inputs through an HTML form.

## Project Structure

- `app.py`: Flask API with advanced logging and HTML UI integration.
- `templates/index.html`: Web UI form for user input.
- `requirements.txt`: Python dependencies file.
- `logs/app.log`: Logs for incoming requests and errors.
- `model.pkl`, `scaler.pkl`, `label_encoders.pkl`, `feature_names.pkl`: Machine learning assets (to be added manually).

## How to Run Locally

1. Clone this repository or unzip the downloaded folder.
2. Make sure your Python environment is set up.
3. Install all required dependencies:
   
   pip install -r requirements.txt
Place your ML model files (model.pkl, scaler.pkl, label_encoders.pkl, feature_names.pkl) into the root project folder.
Run the Flask app: python app.py
Open your browser and go to: http://127.0.0.1:5000/
fill in the form and hit predict to see the results in indian ruppes


Deployment Instructions (Render)
Step 1: Sign In to Render
Go to https://render.com and sign up or log in using your GitHub account.

Step 2: Create a New Web Service
Click "New +" → "Web Service"
Select your GitHub repository that contains the uploaded Flask project.
Step 3: Configure Your Service
Settings:
Name	:housing-price-predictor (or your choice)
Environment	:Python
Build Command	:pip install -r requirements.txt
Start Command	:python app.py
Branch	:main or master (whichever you uploaded to)

Step 4: Deploy
Click "Create Web Service" → Render will:

Install dependencies
Start the server
Expose a public URL for your app (e.g., https://housing-price-predictor.onrender.com)

Step 5: Test It Online
Open the Render URL in your browser.
You’ll see your HTML form.
Submit data — it should return the predicted house price in ₹.


Features
User-friendly HTML UI for predictions.
Currency-formatted predicted price output.
Robust logging using Python’s logging module with rotating log files.
Ready for deployment on platforms like Render, Replit, Railway, etc.
Easy to extend with DVC or MLflow for model versioning .


You're now ready to push this to GitHub and deploy it 
