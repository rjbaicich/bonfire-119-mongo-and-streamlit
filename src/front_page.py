import streamlit as st # Aliasing the streamlit import as st

st.title('Bonfire-119 MTG Tracer Application')
st.text('My first application that uses Pandas, Streamlit, MongoDB, and Python to marry together a Magic Application')

st.header('Here are the different pages of my application:')
st.subheader('Image Return')
st.text('Image Return: Returns an image of the requested card')

st.subheader('Summary')
st.text('Summary: Is a summarization page of all the inner workings of my application and the "why" behind each decision made')

st.subheader('Recommender')
st.text('A recommendation system that we will build if we have the time tomorrow!')