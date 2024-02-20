import streamlit as st

def show_contato():
    st.title("Contato")

    st.write("""
        ## Entre em Contato Conosco
        Tem alguma dúvida, sugestão ou feedback? Ficaremos felizes em ouvir de você!
    """)

    st.subheader("Informações de Contato")
    st.write("""
        **Endereço:** Rua Exemplo, 123 - Cidade, Estado, CEP 12345-678  
        **Telefone:** (12) 3456-7890  
        **E-mail:** contato@exemplo.com
    """)

    st.subheader("Formulário de Contato")
    st.write("""
        Utilize o formulário abaixo para nos enviar uma mensagem diretamente:
    """)
    
    # Adicione campos do formulário, como nome, e-mail, mensagem, etc.
    nome = st.text_input("Seu Nome:")
    email = st.text_input("Seu E-mail:")
    mensagem = st.text_area("Sua Mensagem:")

    if st.button("Enviar Mensagem"):
        # Adicione lógica para processar a mensagem ou enviá-la por e-mail
        st.success("Mensagem enviada com sucesso!")

def main():
    show_contato()

if __name__ == "__main__":
    main()
