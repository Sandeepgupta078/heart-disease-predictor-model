# Heart Disease Predictor

A machine learning application that predicts the likelihood of heart disease based on patient health data. This project includes a web application built with **Streamlit** that allows users to input various health metrics and receive predictions on whether they are at risk for heart disease.

## Overview

This project uses machine learning algorithms to predict the probability of heart disease in patients based on various health metrics such as age, sex, cholesterol levels, blood pressure, and other medical indicators.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis with visualizations
- Model training using Logistic Regression
- Model evaluation and comparison
- Interactive prediction interface

## Installation

```bash
# Clone the repository
git clone https://github.com/Sandeepgupta078/heart-disease-predictor-model.git
cd heart-disease-predictor-model

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

# Start the web interface
```bash
streamlit run app.py
```

## Dataset

The model is trained on the [UCI Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) which includes 14 attributes related to heart health.

## 🏗️ Project Structure

```bash
heart-disease-predictor/
│
├── app.py                       # Main Streamlit app file
├── model/                       # Folder containing trained models (e.g.,    heart_disease_model.sav)
│   ├── heart_disease_model.sav  # Trained model (Pickle file)
├── requirements.txt             # Dependencies required for the app
└── README.md                    # Project information



## 🧑‍💻 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Scikit-learn, Pickle)
- **Machine Learning**: Logistic Regression
- **Data**: Heart Disease dataset

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.