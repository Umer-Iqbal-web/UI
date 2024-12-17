import streamlit as st

# Title and description
st.title("Healthcare Chatbot")
st.write("This chatbot helps identify potential illnesses based on symptoms and suggests medicines. Note: Consult a doctor for professional advice.")

# Symptom-Disease-Medicine Data
data = {
    "fever": {"disease": "Flu", "medicines": ["Paracetamol", "Ibuprofen"]},
    "cough": {"disease": "Common Cold", "medicines": ["Cough Syrup", "Honey"]},
    "headache": {"disease": "Migraine", "medicines": ["Aspirin", "Ibuprofen"]},
    "runny nose": {"disease": "Allergy", "medicines": ["Antihistamines", "Decongestants"]},
    "sore throat": {"disease": "Strep Throat", "medicines": ["Amoxicillin", "Painkillers"]},
}

# User input
symptoms = st.text_input("Enter your symptoms (comma-separated, e.g., fever, headache):")

if st.button("Diagnose"):
    if symptoms:
        input_symptoms = [s.strip().lower() for s in symptoms.split(",")]
        diagnosis = []
        suggested_medicines = []

        for symptom in input_symptoms:
            if symptom in data:
                diagnosis.append(data[symptom]["disease"])
                suggested_medicines.extend(data[symptom]["medicines"])
        
        if diagnosis:
            st.subheader("Possible Diagnosis:")
            st.write(", ".join(set(diagnosis)))

            st.subheader("Suggested Medicines:")
            st.write(", ".join(set(suggested_medicines)))
        else:
            st.warning("No matches found for the entered symptoms. Please consult a doctor.")
    else:
        st.warning("Please enter your symptoms.")

st.write("---")
st.write("**Disclaimer**: This chatbot is for informational purposes only. Always consult a healthcare professional.")
