import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    Cursos = ['Informática', 'Mineração']
    
    with st.form(key='insert'):
        input_course = st.selectbox(label='Insira o curso', options=Cursos)
        input_mat = st.text_input(label='Insira sua matrícula:')
        input_name = st.text_input(label='Insira o nome:')
        input_endereço = st.text_input(label='Insira o seu endereço:')
        input_age = st.number_input(label='Insira a idade', format='%d', step=1)
        
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir( input_course, input_mat, input_name, input_endereço, input_age,)
            st.success('Aluno incluido com sucesso')