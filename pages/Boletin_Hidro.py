import streamlit as st

def show_boletin_hidro():
    st.title("Boletim Hidro")

    st.write("""
        ## Informações sobre Recursos Hídricos
        Bem-vindo ao Boletim Hidro! Aqui você encontrará informações relacionadas aos recursos hídricos, 
        níveis de água, previsões hidrológicas e muito mais.
    """)

    st.subheader("Níveis de Água")
    st.write("""
        Acompanhe os níveis de água em rios, lagos e reservatórios. Informações atualizadas sobre 
        a disponibilidade de água são cruciais para diversas atividades.
    """)

    st.subheader("Previsões Hidrológicas")
    st.write("""
        Conheça as previsões hidrológicas para sua região. Saiba antecipadamente sobre eventos como 
        cheias, estiagens e outras condições que afetam os recursos hídricos.
    """)

    st.subheader("Conservação da Água")
    st.write("""
        Descubra práticas de conservação da água. Dicas para uso eficiente, gestão sustentável 
        e iniciativas para preservação dos recursos hídricos.
    """)

    st.subheader("Projetos Hidráulicos")
    st.write("""
        Explore projetos hidráulicos locais e globais. Desde represas até sistemas de irrigação, 
        fique por dentro das iniciativas que moldam o futuro da gestão da água.
    """)

def main():
    show_boletin_hidro()

if __name__ == "__main__":
    main()
