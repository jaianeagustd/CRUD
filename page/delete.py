import streamlit as st

import controller.cliente as cliente

def excluir():
    st.title('Deletar Dados')

    with st.form(key='delete'):
        nome = st.text_input(label='Insira o nome:')
        buttom_submit = st.form_submit_button('Deletar')

    if buttom_submit:
        cliente.excluir(nome)
        st.success('Aluno excluído com sucesso')
    
