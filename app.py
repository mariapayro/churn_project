import streamlit as st
import joblib
import numpy as np

# Cargar el modelo
modelo = joblib.load("modelo_gradient_boosting.pkl")

st.title("Predicción de cancelación de clientes - Interconnect")

# Entradas del usuario (ejemplo)
monthly_charges = st.number_input("Cargos mensuales:", min_value=0.0)
total_charges = st.number_input("Cargos totales:", min_value=0.0)
senior = st.selectbox("¿Cliente senior?", ["No", "Sí"])
senior = 1 if senior == "Sí" else 0

# Cuando el usuario presiona el botón
if st.button("Predecir"):
    datos = np.array([[monthly_charges, total_charges, senior]])
    pred = modelo.predict(datos)[0]
    if pred == 1:
        st.error("El cliente podría cancelar su contrato.")
    else:
        st.success("El cliente probablemente continúe con el servicio.")
