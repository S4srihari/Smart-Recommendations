# Full-Stack Smart Recommendations with ML Backend

This project is a full-stack web application that provides smart recommendations using a machine learning model. The entire pipeline, from data handling to model deployment, is included.

## Overview

The core of this project is a machine learning model trained to provide recommendations based on user inputs. This model is served via a REST API built with a Python backend. A user-friendly web interface, built with HTML, CSS, and JavaScript, consumes this API to display the smart recommendations to the end-user.

The project demonstrates a complete end-to-end machine learning workflow:
1.  **Data Acquisition:** Gathering the initial data (e.g., `zomatofinal.csv`).
2.  **Data Cleaning & EDA:** Processing the data and performing Exploratory Data Analysis (as seen in `src.ipynb`).
3.  **Model Training:** Experimenting with and training a suitable ML model (e.g., Decision Tree, as saved in `modeldt.pkl`).
4.  **Deployment:** Deploying the model as part of a full-stack web application using Flask.

---

## Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Frontend:** HTML5, CSS, JavaScript
* **Data/Model:** Jupyter Notebook (`src.ipynb`), CSV, Pickle (`modeldt.pkl`)

---

## Project Structure

Here is a brief overview of the key files and directories in this project:

```
├── static/             # Contains static assets (CSS, JS, images)
├── templates/          # Contains HTML templates for the web app
├── app.py              # Main Flask application file (runs the web server and API)
├── modeldt.pkl         # Pre-trained, serialized machine learning model
├── modeldt.py          # Python script used to train and save the ML model
├── src.ipynb           # Jupyter Notebook for data analysis, cleaning, and model experimentation
├── zomatofinal.csv     # Dataset used for training the model
└── ...
```

---

## How It Works

1.  **ML Model:** The `src.ipynb` notebook is used to explore the `zomatofinal.csv` dataset. The data is cleaned, features are engineered, and a machine learning model is trained. The best-performing model is saved as `modeldt.pkl`.
2.  **Backend (API):** The Flask server (`app.py`) loads the pre-trained `modeldt.pkl` model. It exposes one or more API endpoints that receive data from the user (via the frontend). This data is fed into the model to get a prediction/recommendation.
3.  **Frontend (UI):** The user interacts with the HTML pages in the `templates` directory. JavaScript in the `static` folder captures user input and sends an API request to the backend. The frontend then receives the recommendation from the API and displays it to the user.

---

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/S4srihari/Full-Stack-smart-Recommendations-with-ML-on-backend.git](https://github.com/S4srihari/Full-Stack-smart-Recommendations-with-ML-on-backend.git)
    cd Full-Stack-smart-Recommendations-with-ML-on-backend
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    (You may need to create a `requirements.txt` file first. Based on the files, you'll at least need Flask and scikit-learn).
    ```bash
    pip install Flask scikit-learn pandas
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
