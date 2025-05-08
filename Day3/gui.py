import tkinter as tk
import joblib
import numpy as np


# Load the trained model
model = joblib.load('knn_model.pkl')

# Initialize the Tkinter window
window = tk.Tk()
window.title("Iris Species Predictor")

# Create input labels and fields for features
features = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
inputs = {}

for i, feature in enumerate(features):
    label = tk.Label(window, text=feature)
    label.grid(row=i, column=0, padx=10, pady=5)
    input_field = tk.Entry(window)
    input_field.grid(row=i, column=1, padx=10, pady=5)
    inputs[feature] = input_field

# Create a label to display the prediction result
prediction_label = tk.Label(window, text="Prediction: ", font=("Arial", 12))
prediction_label.grid(row=len(features), column=0, columnspan=2, pady=10)

# Prediction function
def predict_species():
    try:
        # Get user input values
        feature_values = [float(inputs[feature].get()) for feature in features]
        feature_values = np.array(feature_values).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(feature_values)
        class_names = ['setosa', 'versicolor', 'virginica']  # Adjust based on your model
        predicted_class = prediction[0]

        # Update the prediction label with the result
        prediction_label.config(text=f"Prediction: {predicted_class}")

    except ValueError:
        prediction_label.config(text="Prediction: Invalid input. Please enter numeric values.")

# Create the Predict button
predict_button = tk.Button(window, text="Predict", command=predict_species)
predict_button.grid(row=len(features)+1, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
window.mainloop()
