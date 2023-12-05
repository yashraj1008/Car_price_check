import pickle
import streamlit as st
import numpy as np

loaded_model = pickle.load(open('//car_model.sav','rb'))

st.title('Car Price Predictor')

Year = st.text_input('Year of Manufacture')
Present_Price = st.text_input('Present Price')
Kms_Driven = st.text_input('Kms Driven')
Fuel_Type = st.text_input('Fuel Type')
Seller_Type = st.text_input('Seller Type (Dealer, Individual...etc)')
Transmission = st.text_input('Transmission Type')
Owner = st.text_input('Previoius Owners')

input_data = np.array9[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]
input_reshaped = input_data.reshape(1,-1)

price_pred =''

if st.button('Check Price'):
    car_price = loaded_model.predict(input_reshaped)

    if(car_price[0]==0):
        price_pred = (car_price)
    else:
        price_pred = 'Sorry...'
st.success(price_pred)
