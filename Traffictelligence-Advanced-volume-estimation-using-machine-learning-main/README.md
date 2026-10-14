# 🚦 Traffictelligence: Advanced Traffic Volume Estimation Using Machine Learning

## 📌 Project Overview

**Traffictelligence** is a machine learning project designed to estimate traffic volume using historical traffic data, weather conditions, holidays, and date-time information.

The project compares multiple regression algorithms and provides a web application built with Flask, allowing users to enter environmental and date-time details and receive an estimated traffic volume.

**Note:** The application generates model-based predictions. It does not currently use a live traffic data feed.

## 🎯 Objectives

- Estimate traffic volume using historical data.
- Analyze the relationship between weather conditions and traffic patterns.
- Compare machine learning regression algorithms.
- Evaluate model performance using regression metrics.
- Build a web application for interactive predictions.
- Demonstrate an end-to-end machine learning workflow.

## ✨ Features

- Traffic volume estimation using machine learning.
- Weather and holiday-based inputs.
- Date and time inputs.
- Interactive Flask web application.
- Input validation for numerical values, dates, and time.
- Saved machine learning pipeline for predictions.
- Responsive HTML and CSS interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing, model evaluation, and machine learning |
| XGBoost | Gradient boosting regression |
| Flask | Web application backend |
| Joblib | Saving and loading the model |
| HTML and CSS | User interface |
| Jupyter Notebook | Data analysis and model development |

## 📂 Project Structure

```text
Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/
├── README.md
├── Document/
│   ├── Traffictelligence.docx
│   └── readme.md
├── Project Files/
│   ├── Code.ipynb
│   ├── app.py
│   ├── readme.md
│   ├── traffic volume.csv
│   ├── traffictelligence_best_model.joblib
│   ├── traffictelligence_final_model.joblib
│   └── templates/
│       ├── index.html
│       └── readme.md
└── Video Demonstration/
    ├── video demo(1)(1).mp4
    └── readme.md
```

## 📊 Dataset

The project uses a historical traffic volume dataset located at `Project Files/traffic volume.csv`.

The dataset contains the following columns:

| Feature | Description |
|---|---|
| `holiday` | Holiday information |
| `temp` | Temperature |
| `rain` | Rainfall measurement |
| `snow` | Snowfall measurement |
| `weather` | Weather condition |
| `date` | Date information |
| `Time` | Time information |
| `traffic_volume` | Observed traffic volume and prediction target |

Date and time information are processed into features such as year, month, day, hours, minutes, and seconds.

## 🤖 Machine Learning Models

The project compares multiple regression algorithms:

- XGBoost Regressor
- Random Forest Regressor
- Decision Tree Regressor
- Support Vector Regression (SVR)
- Linear Regression

### Model Comparison

The recorded model evaluation results are:

| Model | R² Score |
|---|---:|
| XGBoost Regressor | 0.8222 |
| Random Forest Regressor | 0.7879 |
| Decision Tree Regressor | 0.6685 |
| Support Vector Regression | 0.2614 |
| Linear Regression | 0.1500 |

**Selected model:** XGBoost Regressor.

The recorded XGBoost evaluation results are:

- **R² Score:** 0.8222
- **Mean Absolute Error (MAE):** 553.72
- **Root Mean Squared Error (RMSE):** 838.50

These metrics describe the project's recorded test-set evaluation. Performance may vary with different datasets, test splits, and deployment conditions.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/prudeeshwar3363/AI-ML-projects.git
```

### 2. Navigate to the project directory

Open a terminal and run:

```powershell
cd "AI-ML-projects\Traffictelligence-Advanced-volume-estimation-using-machine-learning-main\Project Files"
```

Adjust the path if your local folder structure differs.

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

The project folder currently does not contain a `requirements.txt` file. Install the main application dependencies using:

```bash
python -m pip install Flask pandas numpy scikit-learn xgboost joblib
```

For reproducible results, use package versions compatible with those used to train and save the model.

### 5. Run the Flask application

Ensure that the following files are available in the `Project Files` directory:

- `app.py`
- `traffictelligence_final_model.joblib`
- `templates/index.html`

Start the application:

```bash
python app.py
```

### 6. Open the application

Open your browser and visit:

**http://127.0.0.1:5000**

Enter the required weather, holiday, date, and time values, then submit the form to view the estimated traffic volume.

## 🔄 How It Works

1. **Data collection:** Load the historical traffic volume dataset.
2. **Data preprocessing:** Prepare numerical and categorical features.
3. **Feature engineering:** Extract useful components from date and time information.
4. **Model training:** Train and compare regression algorithms.
5. **Model evaluation:** Evaluate performance using R², MAE, and RMSE.
6. **Model persistence:** Save the selected model pipeline using Joblib.
7. **User input:** Collect prediction details through the Flask interface.
8. **Prediction:** Pass the inputs through the saved preprocessing and model pipeline.
9. **Result display:** Display the estimated traffic volume on the webpage.

## 📈 Evaluation Metrics

### R² Score

Measures how much variation in the target variable is explained by the regression model.

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted traffic volume.

### Root Mean Squared Error (RMSE)

Measures prediction error while penalizing larger errors more strongly.

### Recorded XGBoost Results

| Metric | Value |
|---|---:|
| R² Score | 0.8222 |
| MAE | 553.72 |
| RMSE | 838.50 |

## 🎥 Project Resources

- [View the project repository](https://github.com/prudeeshwar3363/AI-ML-projects/tree/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main)
- [View the Jupyter Notebook](https://github.com/prudeeshwar3363/AI-ML-projects/blob/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/Project%20Files/Code.ipynb)
- [View the Flask application](https://github.com/prudeeshwar3363/AI-ML-projects/blob/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/Project%20Files/app.py)
- [View the web interface](https://github.com/prudeeshwar3363/AI-ML-projects/blob/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/Project%20Files/templates/index.html)
- [View the project report](https://github.com/prudeeshwar3363/AI-ML-projects/blob/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/Document/Traffictelligence.docx)
- [View the video demonstration](https://github.com/prudeeshwar3363/AI-ML-projects/blob/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main/Video%20Demonstration/video%20demo%281%29%281%29.mp4)

## 🚀 Future Improvements

- Add traffic trend visualizations.
- Improve model performance through further experimentation.
- Add automated tests for application inputs and predictions.
- Deploy the application to a cloud hosting platform.
- Compare actual and predicted traffic volume.
- Integrate a reliable real-time traffic data source.
- Add a `requirements.txt` file with tested dependency versions.

## 👨‍💻 Author

**Prudveeswar**

- **GitHub:** [@prudeeshwar3363](https://github.com/prudeeshwar3363)
- **Repository:** [AI-ML-projects/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main](https://github.com/prudeeshwar3363/AI-ML-projects/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main)
