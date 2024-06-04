import pickle
import streamlit as st

# membaca model
obesitas_model = pickle.load(open('obesitas_model1.sav'))

#judul
st.title('Prediksi Obesitas')