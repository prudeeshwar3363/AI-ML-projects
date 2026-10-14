# 🚦 Traffictelligence: Advanced Traffic Volume Estimation Using Machine Learning

## 📌 Project Overview

**Traffictelligence** is a machine learning project that predicts traffic volume based on weather conditions, holidays, and date-time information. It uses historical traffic data to estimate the number of vehicles under different conditions.

The project includes a trained machine learning model and a web application built with Flask, allowing users to enter input values and receive traffic volume predictions through a simple interface.

## 🎯 Objectives

- Predict traffic volume using historical data.
- Analyze the relationship between weather conditions and traffic patterns.
- Compare multiple machine learning algorithms.
- Build a web application for interactive predictions.
- Demonstrate an end-to-end machine learning workflow.

## ✨ Features

- Traffic volume prediction using machine learning.
- Weather and holiday-based input parameters.
- Date and time feature inputs.
- Interactive web interface built with Flask.
- Input validation for numeric values, dates, and time.
- Saved machine learning pipeline for predictions.
- Responsive dark-themed user interface.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** XGBoost, Random Forest, Decision Tree, Support Vector Regression, Linear Regression
- **Data Processing:** Pandas, NumPy
- **Machine Learning Tools:** Scikit-learn, XGBoost
- **Web Framework:** Flask
- **Model Persistence:** Joblib
- **Frontend:** HTML, CSS

## 📂 Project Structure

```text
Traffictelligence/
├── Project Files/
│   ├── app.py
│   ├── Code.ipynb
│   ├── traffic volume.csv
│   ├── traffictelligence_final_model.joblib
│   └── templates/
│       └── index.html
├── README.md
└── requirements.txt
```

*Note: The structure above represents the expected application layout. Adjust it to match the actual files in your repository.*

## 📊 Dataset

The project uses a historical traffic volume dataset containing the following features:

| Feature | Description |
|---|---|
| `holiday` | Holiday information |
| `temp` | Temperature |
| `rain` | Rainfall measurement |
| `snow` | Snowfall measurement |
| `weather` | Weather condition |
| `date` | Original date information |
| `Time` | Original time information |
| `traffic_volume` | Target variable: observed traffic volume |

Date and time information are processed into features such as year, month, day, hour, minute, and second.

## 🤖 Machine Learning Models

The project compares multiple regression algorithms to identify a suitable model for traffic volume estimation.

| Model | R² Score |
|---|---:|
| XGBoost Regressor | 0.8222 |
| Random Forest Regressor | 0.7879 |
| Decision Tree Regressor | 0.6685 |
| Support Vector Regression | 0.2614 |
| Linear Regression | 0.1500 |

**Selected model:** XGBoost Regressor.

The original XGBoost model achieved an R² score of approximately **0.82** on the evaluation test set. These results reflect the project's recorded evaluation and may vary with different data splits or configurations.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/prudeeshwar3363/AI-ML-projects.git
```

### 2. Navigate to the project directory

```bash
cd AI-ML-projects/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/Project\ Files
```

Adjust the directory name if your local folder differs.

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

Create a `requirements.txt` file containing the packages required by your application, then run:

```bash
pip install -r requirements.txt
```

Typical dependencies include:

```text
Flask
pandas
numpy
scikit-learn
xgboost
joblib
```

Use compatible package versions for the environment in which the model was trained and tested.

### 5. Run the application

Ensure that `app.py`, `traffictelligence_final_model.joblib`, and the `templates/index.html` file are in the expected locations.

```bash
python app.py
```

### 6. Open the web application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

Enter the weather, holiday, date, and time details, then submit the form to view the estimated traffic volume.

## 🔄 How It Works

1. **Data collection:** Load the historical traffic volume dataset.
2. **Data preprocessing:** Prepare categorical, numerical, date, and time features.
3. **Model training:** Train and compare regression models.
4. **Model evaluation:** Evaluate predictions using regression metrics.
5. **Model saving:** Save the selected model pipeline using Joblib.
6. **User input:** Collect prediction inputs through the Flask web interface.
7. **Prediction:** Process the inputs through the saved pipeline.
8. **Display:** Show the estimated number of vehicles on the webpage.

## 📈 Evaluation Metrics

The project uses regression evaluation metrics, including:

- **R² Score:** Measures how much variation in the target is explained by the model.
- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted traffic volume.
- **RMSE (Root Mean Squared Error):** Penalizes larger prediction errors more strongly.

Recorded results for the original XGBoost model:

- **R² Score:** 0.8222
- **MAE:** 553.72
- **RMSE:** 838.50

These metrics are dataset- and test-split-dependent and should not be interpreted as guaranteed real-world accuracy.

## 🚀 Future Improvements

- Add interactive traffic trend visualizations.
- Improve model performance through further experimentation.
- Add automated tests for prediction inputs and model outputs.
- Deploy the application to a cloud platform.
- Add historical versus predicted traffic comparisons.
- Extend the system with real-time traffic data where available.

## 👨‍💻 Author

**Prudveeswar**

- GitHub: [@prudeeshwar3363](https://github.com/prudeeshwar3363)
- Project Repository: [AI-ML-projects](https://github.com/prudeeshwar3363/AI-ML-projects)
