import streamlit as st

import controller.cliente as cliente

def atualizar():
    st.title('Atualizar Dados')

    with st.form(key='update'):
        matrícula = st.text_input(label='Insira a sua matrícula:')
        buttom_submit = st.form_submit_button('Atualizar')

    if buttom_submit:
        cliente.atualizar(matrícula)
        st.success('Dado atualizado com sucesso')
    