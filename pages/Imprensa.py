import streamlit as st

def show_imprensa():
    st.title("Imprensa")

    st.write("""
        ## Últimas Notícias e Comunicados de Imprensa
        Fique por dentro das últimas notícias e comunicados de imprensa relacionados às estações meteorológicas.
    """)

    st.subheader("Notícias Recentes")
    # Adicione seções de notícias recentes com links para artigos ou comunicados

    st.markdown("""
        - [Título da Notícia 1](#)
        - [Título da Notícia 2](#)
        - [Título da Notícia 3](#)
    """)

    st.subheader("Comunicados de Imprensa")
    # Adicione seções de comunicados de imprensa com links para releases ou anúncios

    st.markdown("""
        - [Comunicado de Imprensa 1](#)
        - [Comunicado de Imprensa 2](#)
        - [Comunicado de Imprensa 3](#)
    """)

def main():
    show_imprensa()

if __name__ == "__main__":
    main()