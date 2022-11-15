import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman : ', ('Exploratory Data Analysis', 'Predict Fire Alarm'))

if navigation == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()

# Ctrl + C = Terminate
# streamlit run 'filename'

# heroku login
# git init
# git add .
# git status
# git commit -m "Add files"
# heroku create "webname"
# git push heroku main