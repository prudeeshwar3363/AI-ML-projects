# Traffictelligence: Vehicle Volume Estimation Using Machine Learning

## Project Overview
Traffictelligence is a machine learning project designed to estimate traffic volume using historical traffic and weather data. It explores regression models to predict vehicle volume and evaluate their performance.

## Objectives
- Prepare and clean traffic volume data.
- Explore relationships between weather conditions and traffic volume.
- Train and compare machine learning regression models.
- Evaluate model performance using regression metrics.

## Technologies Used
- Python
- Pandas and NumPy
- Seaborn and Matplotlib
- scikit-learn
- XGBoost
- Jupyter Notebook

## Dataset
The project includes `traffic volume.csv`, containing traffic volume, temperature, rain, snow, weather, date, time, and holiday information.

## Methodology
1. Load and inspect the dataset.
2. Handle missing values in selected columns.
3. Explore data distributions and correlations.
4. Extract date and time components.
5. Scale features and split the dataset into training and testing sets.
6. Train and compare Linear Regression, Decision Tree, Random Forest, Support Vector Regression, and XGBoost regression models.
7. Evaluate predictions using regression metrics.

## Project Structure
- `Project Files/Code.ipynb` — data analysis and machine learning workflow.
- `Project Files/traffic volume.csv` — traffic dataset.
- `Project Files/app.py` — application file, if applicable.
- `Project Files/index.html` — interface file, if applicable.
- `Document/` — project documentation.
- `Video Demonstration/` — project demonstration materials.

## Results
The notebook evaluates multiple regression models. Exact performance results should be reported after verifying the test-set metrics and selecting the best-performing model.

## Future Improvements
- Improve feature engineering and categorical encoding.
- Compare models using appropriate regression metrics, including R², MAE, and RMSE.
- Validate the best model with consistent preprocessing and reproducible experiments.
- Document application setup and prediction instructions.

## Project Repository
[View the source code on GitHub](https://github.com/prudeeshwar3363/AI-ML-projects/tree/main/Traffictelligence-Advanced-volume-estimation-using-machine-learning-main)
