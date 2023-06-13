import streamlit as st

st.title('My Streamlit App')
st.write('Welcome to my app!')

options = ['APPLE', 'GOOGLE', 'MICROSOFT']
selected_option = st.selectbox('Select an option', options)

if st.button('Submit'):
    st.write('You selected:', selected_option)
