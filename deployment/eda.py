import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    # Membuat Title
    st.title('Exploratory Data Analysis')

    # Membuat Sub Header
    st.subheader('EDA untuk Analisa Dataset Smoke Detection')

    # Membuat Deskripsi
    st.write('Page ini dibuat oleh *Steven Kusuma - FTDS Batch 015 - Milestone 2*')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    st.write('''
    Dataset yang digunakan adalah dataset Smoke Detection.
    Dataset ini berasal dari web https://www.kaggle.com/datasets/deepcontractor/smoke-detection-dataset.
    ''')

    # Show DataFrame
    data = pd.read_csv('h8dsft_Milestone2P1_Steven_Kusuma.csv')
    st.dataframe(data)

    # Heatmap
    st.write('#### Heatmap')
    fig = plt.figure(figsize=(15, 15))
    sns.heatmap(data.corr(), annot=True)
    st.pyplot(fig)
    st.write('5 Features ini adalah yang korelasinya tertinggi dengan target Fire Alarm')

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
