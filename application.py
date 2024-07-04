import streamlit as st
import numpy as np
import pandas as pd
import pickle

app = appplicaiton

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/previews/006/852/804/original/abstract-blue-background-simple-design-for-your-website-free-vector.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Anemia Classification')
scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))
logistic_model = pickle.load(open('models/Logistic.pkl', 'rb'))

RedPixel = st.slider('Input Value For Percent Of Red Pixel: ',0.00,100.00,43.14)
GreenPixel = st.slider('Input Value For Percent Of Green Pixel: ',0.00,100.00,30.16)
BluePixel = st.slider('Input Value For Percent Of Blue Pixel: ',0.00,100.00,26.69)
HB = st.slider('Input Level Of Hemoglobin In Blood: ',0.00,50.00,8.6)

columns = ['Red Pixel', 'Green Pixel', 'Blue Pixel', 'Hb']
def predict():
    row = np.array([RedPixel, GreenPixel, BluePixel, HB])
    X = pd.DataFrame([row], columns = columns)
    X_scaled = scaler_model.transform(X)
    prediction = logistic_model.predict(X_scaled)[0]
    if prediction == 1:
        st.success('Anaemic: Yes')
    else:
        st.error('Anaemic: No')

st.button('Predict', on_click=predict)
st.markdown("---")
st.write('The Color Composition Of Pixels Are Using The Device Which Creates Constant Light, Captures The Palpebral Conjuctiva, Generating The Masked Photo With ROI To Give The Values For Pixels And Hemoglobin')
