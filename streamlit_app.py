try:
    import streamlit as st
    import os
    from fastapi import FastAPI 
except:
    os.system('pip install -r requirements.txt')

st.title('My Streamlit App')
st.write('Welcome to my app!')

options = ['CAROL', 'CHRISTIAN']
selected_option = st.selectbox('Select an option', options)

if st.button('Submit'):
    st.write('You selected:', selected_option)
    if selected_option == 'CAROL': st.write('CAROL ES LA CANARIA MÁS GUAPA, ME IRÍA DE VIAJE 1 AÑO CON ELLA💛💛💛')
    elif selected_option == 'CHRISTIAN': st.write('QUIERES VIVIR CONMIGO ESTE VERANO Y HACER EL CONEJITO TODOS LOS DIAS??🦔💘🦝 ')

app =FastAPI()
 #https://ominous-enigma-6w7645wqq44f4gw4-8000.app.github.dev/ 
@app.get('/intro') 
def index(): 
   return 'FASTAPI'

