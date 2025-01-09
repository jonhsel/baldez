import streamlit as st


TIPOS_ARQUIVOS = ['Site', 'Youtube', 'pdf', 'csv', 'txt']

CONFIG_MODELOS = {  'OpenAI': {'modelos': ['gpt-4o-mini', 'gpt-4o']}

}

def pagina_chat():
    st.header('⚖️ Assistente do Jonh Selmo - CAOJÚRI')

    mensagens = st.session_state.get('mensagens', [])
    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])

    input_usuario = st.chat_input('Fale com o Assistente!')
    if input_usuario:
        mensagens.append(('user', input_usuario))
        st.session_state['mensagens'] = mensagens
        st._rerun()
        
def sidebar():
    tabs_assistente = st.tabs(['Uploads de Arquivos', 'Modelo de IA'])
    with tabs_assistente[0]:
        tipo_arquivo = st.selectbox('selecione o tipo de URL ou arquivo', TIPOS_ARQUIVOS)
        if tipo_arquivo == 'Site':
            arquivo = st.text_input('Digite a URL do site')
        if tipo_arquivo == 'Youtube':
            arquivo = st.text_input('Digite a URL do Youtube')
        if tipo_arquivo == 'pdf':
            arquivo = st.file_uploader('Carregue o arquivo do tipo .pdf', type=['.pdf'])
        if tipo_arquivo == 'csv':
            arquivo = st.file_uploader('Carregue o arquivo do tipo .csv', type=['.csv'])
        if tipo_arquivo == 'txt':
            arquivo = st.file_uploader('Carregue o arquivo do tipo .txt', type=['.txt'])
        
    with tabs_assistente[1]:
        provedor = st.selectbox('Selecione a empresa criadora do modelo de IA', CONFIG_MODELOS.keys())
        modelo = st.selectbox('Selecione o modelo de IA', CONFIG_MODELOS[provedor]['modelos'])
        api_key = st.text_input(
            f'Adicione a API do modelo escolhido{provedor}',
            value=st.session_state.get(f'api_key_{provedor}')
        )
        st.session_state[f'api_key_{provedor}'] = api_key

def main():
    pagina_chat()
    with st.sidebar:
        sidebar()

if __name__=='__main__':
    main()