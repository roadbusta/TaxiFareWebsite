import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''


pickup_date = st.date_input(
                    'Set pickup date',
                    datetime.date(2021,9,15)
                            )


pickup_time = st.time_input(
                            'Set pickup time',
                           datetime.time(9,00)
                           )

pickup_longitude = st.number_input('Set pickup longitude', 40.7614327, format ='%.5f')
pickup_latitude = st.number_input('Set pickup latitude', -73.9798156, format='%.5f')
dropoff_longitude = st.number_input('Set dropoff longitude', 40.6513111, format='%.5f')
dropoff_latitude = st.number_input('Set dropoff latitude', -73.8803331, format='%.5f')
passenger_count = st.number_input('Set passenger count', 2, format = '%d')

'''
# Summary
'''
st.write('The pickup date is: ', pickup_date)
st.write('The pickup time is: ', pickup_time)
st.write('The pickup longitude is: ', pickup_longitude)
st.write('The pickup latitude is: ', pickup_latitude)
st.write('The dropoff longitude is: ', dropoff_longitude)
st.write('The dropoff latitude is :', dropoff_latitude)
st.write('The passenger count is: ', passenger_count)

# if url == 'https://taxifare.lewagon.ai/predict':

# st.markdown(
#     'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
# )

dt_string = f"{pickup_date}%{pickup_date.strftime('%Y')}:{pickup_time.strftime('%H:%M')}"
params = {
    "pickup_datetime": dt_string,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}
url = 'https://taxifare.lewagon.ai/predict'
url_string = f"{url}?pickup_datetime={dt_string}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={passenger_count}"

r = requests.get(url_string).json()

st.write("Predicted fare price is: $%.2f" % r['prediction'])

#Why doesn't this work
# r = requests.get(url, params = params).json()
# st.write("Predicted fare price is:" , r)
