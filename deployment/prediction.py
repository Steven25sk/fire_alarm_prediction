import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import json

# Load Model
with open('deployment/pipe_rf.pkl', 'rb') as file_1:
  pipe_rf = joblib.load(file_1) 

def run():
    # Membuat Form
    with st.form(key='form_parameters'):
        temperature = st.number_input('Temperature[C]', min_value=-22.010, max_value=59.930, value=20.000, help='Temperature C')
        humidity = st.number_input('Humidity[%]', min_value=10.740, max_value=75.200, value=45.000, help='Humidity %')
        TVOC = st.number_input('TVOC[ppb]', min_value=0.000, max_value=60000.000, value=1000.000, help='Total Volatile Organic Compound')
        raw_ethanol = st.number_input('Raw Ethanol', min_value=15317.000, max_value=21410.000, value=17500.000, help='Raw Ethanol')
        pressure = st.number_input('Pressure[hPa]', min_value=930.852, max_value=939.861, value=939.000, help='Pressure')
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'Temperature[C]': temperature,
        'Humidity[%]': humidity,
        'TVOC[ppb]': TVOC,
        'Raw Ethanol': raw_ethanol,
        'Pressure[hPa]': pressure
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Predict using Random Forest
        y_pred_inf_rf = pipe_rf.predict(data_inf)
        
        st.write('## Fire Alarm : ' + str(int(y_pred_inf_rf)))

if __name__ == '__main__':
    run()

# Ctrl + C = Terminate
# streamlit run 'filename'

# heroku login
# git init
# git add .
# git status
# git commit -m "Add files"
# heroku create "webname"
# git push heroku main
