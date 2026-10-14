
from flask import Flask, request, render_template
from pathlib import Path
import datetime
import joblib
import pandas as pd
import math

app = Flask(__name__)

# Locate project files
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "traffictelligence_final_model.joblib"

print("App folder:", BASE_DIR)
print("Template folder:", BASE_DIR / "templates")

# Load the saved model pipeline
saved_model = joblib.load(MODEL_PATH)
model = saved_model["pipeline"]
feature_columns = saved_model["feature_columns"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read categorical inputs
        holiday = request.form.get("holiday", "None")
        weather = request.form.get("weather", "Clouds")

        # Read numerical inputs
        input_values = {
            "holiday": holiday,
            "temp": float(request.form["temp"]),
            "rain": float(request.form["rain"]),
            "snow": float(request.form["snow"]),
            "weather": weather,
            "year": float(request.form["year"]),
            "month": float(request.form["month"]),
            "day": float(request.form["day"]),
            "hours": float(request.form["hours"]),
            "minutes": float(request.form["minutes"]),
            "seconds": float(request.form["seconds"])
        }

        # Reject NaN and infinite numeric values
        numeric_fields = [
            "temp", "rain", "snow", "year", "month",
            "day", "hours", "minutes", "seconds"
        ]

        for field in numeric_fields:
            if not math.isfinite(input_values[field]):
                raise ValueError(f"{field} must be a finite number.")

        # Validate temperature and precipitation
        if not 0 <= input_values["temp"] <= 350:
            raise ValueError(
                "Temperature must be between 0 and 350 Kelvin."
            )

        if input_values["rain"] < 0 or input_values["snow"] < 0:
            raise ValueError("Rain and snow cannot be negative.")

        # Validate year, month, and calendar date
        if not 2012 <= input_values["year"] <= 2022:
            raise ValueError("Year must be between 2012 and 2022.")

        if not input_values["year"].is_integer():
            raise ValueError("Year must be a whole number.")

        if not input_values["month"].is_integer():
            raise ValueError("Month must be a whole number.")

        if not input_values["day"].is_integer():
            raise ValueError("Day must be a whole number.")

        try:
            datetime.date(
                int(input_values["year"]),
                int(input_values["month"]),
                int(input_values["day"])
            )
        except ValueError:
            raise ValueError("Please enter a valid calendar date.")

        # Validate time
        for field, minimum, maximum in [
            ("hours", 0, 23),
            ("minutes", 0, 59),
            ("seconds", 0, 59)
        ]:
            value = input_values[field]

            if not value.is_integer() or not minimum <= value <= maximum:
                raise ValueError(
                    f"{field.capitalize()} must be a whole number "
                    f"between {minimum} and {maximum}."
                )

        # Validate model feature names
        missing_features = [
            col for col in feature_columns
            if col not in input_values
        ]

        if missing_features:
            raise ValueError(
                "Missing model features: " + ", ".join(missing_features)
            )

        # Prepare model input in the training feature order
        input_df = pd.DataFrame(
            [{col: input_values[col] for col in feature_columns}],
            columns=feature_columns
        )

        # Predict using the complete preprocessing pipeline
        prediction = float(model.predict(input_df)[0])

        # Traffic volume cannot be negative
        prediction = max(0, prediction)

        return render_template(
            "index.html",
            prediction_text=f"{round(prediction):,}",
            prediction_error=False
        )

    except (ValueError, KeyError) as error:
        return render_template(
            "index.html",
            prediction_text=f"Invalid input: {error}",
            prediction_error=True
        ), 400

    except Exception:
        app.logger.exception("Unexpected prediction error")
        return render_template(
            "index.html",
            prediction_text=(
                "Prediction failed. Please check the model "
                "and input configuration."
            ),
            prediction_error=True
        ), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
