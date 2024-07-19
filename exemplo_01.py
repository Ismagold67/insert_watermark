import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Exibidor de arquivos
            
## Suba um arquivo e vejamos o que acontece 😎😎
            ''')

st.text_input("Email")
st.text_input("Senha", type='password')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!!',
    type=['jpg', 'png', 'py', 'wav', 'csv', 'json']
)

if arquivo:
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio', _:
            st.audio(arquivo)
        case 'video', _:
            st.video(arquivo)
else:
    st.error('Ainda não tenho arquivo!')
