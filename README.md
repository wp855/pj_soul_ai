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
Push this code to a GitHub repository.
Go to https://render.com and create an account or sign in.
Click "New Web Service" and connect your GitHub repo.
Set the build and start commands:
Build Command: pip install -r requirements.txt
Start Command: python app.py
Deploy the app and get a public URL to share.


Features
User-friendly HTML UI for predictions.
Currency-formatted predicted price output.
Robust logging using Python’s logging module with rotating log files.
Ready for deployment on platforms like Render, Replit, Railway, etc.
Easy to extend with DVC or MLflow for model versioning .


You're now ready to push this to GitHub and deploy it 
