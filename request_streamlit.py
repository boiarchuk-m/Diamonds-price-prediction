import streamlit as st
import requests

#url = f'http://localhost:9696/predict'
url = 'https://diamonds-l4pdyslp4q-uc.a.run.app/predict'

st.header('Diamonds price prediction')

shape = st.selectbox('Choose diamond shape', ('Round', 'Emerald', 'Marquise', 'Princess', 'Pear',
                                           'Heart', 'Oval', 'Cushion', 'Asscher', 'Radiant'))
carat = st.number_input('Insert diamond carat', min_value=0.01, value=0.08, max_value=30.0)
cut = st.selectbox('Choose cut quality', ('Very Good', 'Ideal', 'Super Ideal', 'Good', 'Fair'))

color = st.selectbox('Choose diamond color', ('J', 'I', 'E', 'F', 'G', 'H', 'D'))

clarity = st.selectbox('Choose diamond clarity', ('SI2', 'SI1', 'VS2', 'VVS1', 'VS1', 'VVS2', 'IF', 'FL'))

report = st.selectbox('Choose lab', ('GIA', 'HRD', 'IGI', 'GCAL'))

type =st.selectbox('Choose diamond type', ('natural', 'lab'))

dict_data={'shape': shape,'carat': carat, 'cut': cut, 'color': color, 'clarity': clarity,
            'report': report, 'type': type}


button = st.button("Predict")
if button:
    response = requests.post(url, json=dict_data).json()
    st.write('Value: ', response['Value'], '$')
