import pickle
import streamlit as st
import os

# Set page config
st.set_page_config(page_title="Heart Disease Predictor ❤️", layout="centered", page_icon="❤️")

# Title
st.title("💓 Heart Disease Prediction using Machine Learning")

st.markdown("""
This application predicts whether a person is likely to have heart disease based on various health metrics.  
Fill out the form below and click **Predict** to see your result.
""")

# Load the model
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, 'model/heart_disease_model.sav')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Input feature explanations
with st.expander("ℹ️ Feature Descriptions"):
    st.markdown("""
    - **Age**: Age of the person (in years)
    - **Sex**: 1 = Male, 0 = Female
    - **Chest Pain Type (cp)**: 
        - 0: Typical angina
        - 1: Atypical angina
        - 2: Non-anginal pain
        - 3: Asymptomatic
    - **Resting Blood Pressure (trestbps)**: In mm Hg
    - **Serum Cholesterol (chol)**: In mg/dl
    - **Fasting Blood Sugar > 120 (fbs)**: 1 = True, 0 = False
    - **Resting ECG results (restecg)**:
        - 0: Normal
        - 1: Having ST-T wave abnormality
        - 2: Showing probable/definite left ventricular hypertrophy
    - **Max Heart Rate Achieved (thalach)**: Beats per minute
    - **Exercise Induced Angina (exang)**: 1 = Yes, 0 = No
    - **Oldpeak**: ST depression induced by exercise relative to rest
    - **Slope**: The slope of the peak exercise ST segment (0–2)
    - **ca**: Number of major vessels colored by fluoroscopy (0–3)
    - **thal**:
        - 1: Normal
        - 2: Fixed defect
        - 3: Reversible defect
    """)

# Input form
with st.form("input_form"):
    st.subheader("📝 Enter Patient Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=45)
        sex = st.selectbox("Sex", options=["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", value=120)
        chol = st.number_input("Cholesterol (mg/dl)", value=200)
        fbs = st.selectbox("Fasting Blood Sugar > 120?", options=["Yes", "No"])

    with col2:
        restecg = st.selectbox("Resting ECG Results", options=["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"])
        thalach = st.number_input("Max Heart Rate Achieved", value=150)
        exang = st.selectbox("Exercise Induced Angina", options=["Yes", "No"])
        oldpeak = st.number_input("Oldpeak", value=1.0)
        slope = st.selectbox("Slope of ST Segment", options=["Upsloping", "Flat", "Downsloping"])
        ca = st.selectbox("Major Vessels Colored (0–3)", options=[0, 1, 2, 3])
        thal = st.selectbox("Thalassemia Type", options=["Normal", "Fixed Defect", "Reversible Defect"])

    submit = st.form_submit_button("🔍 Predict")

    if submit:
        # Map inputs to numerical values
        sex_val = 1 if sex == "Male" else 0
        cp_val = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
        fbs_val = 1 if fbs == "Yes" else 0
        restecg_val = ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"].index(restecg)
        exang_val = 1 if exang == "Yes" else 0
        slope_val = ["Upsloping", "Flat", "Downsloping"].index(slope)
        thal_val = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal) + 1  # model expects 1–3

        user_data = [age, sex_val, cp_val, trestbps, chol, fbs_val,
                     restecg_val, thalach, exang_val, oldpeak, slope_val, ca, thal_val]

        prediction = model.predict([user_data])

        st.subheader("🧠 Prediction Result")
        if prediction[0] == 1:
            st.error("⚠️ The person **is likely to have heart disease**.")
        else:
            st.success("✅ The person **does NOT have heart disease**.")

# Optional footer
st.markdown("""
---
### 👨‍💻 Developed by [Sandeep](https://sandeepgupta.vercel.app)

🔗 **Connect with me:**

- [GitHub](https://github.com/Sandeepgupta078)
- [LinkedIn](https://www.linkedin.com/in/sandeepg75/)
- [Email](mailto:sandeepmgs078@gmail.com)

Built using [Streamlit](https://streamlit.io) ❤️
""")

