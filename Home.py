import streamlit as st
from mapa import return_map

def main():
    st.set_page_config(
        page_title="STREAMLIT MAPA",
        page_icon="🌍",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    st.title("Página Home")

    st.write("""
        ### Legenda de Cores

        - **INCAPER:** <span style="color: green; font-weight: bold;">■</span> Verde
        - **CEPDEC:** <span style="color: orange; font-weight: bold;">■</span> Laranja
        - **ANA:** <span style="color: blue; font-weight: bold;">■</span> Azul
        - **INMET:** <span style="color: red; font-weight: bold;">■</span> Vermelho

        """, unsafe_allow_html=True)
    
    return_map()

    st.write("""
        ### Sobre as Instituições

        - **INCAPER:**
            - O Instituto Capixaba de Pesquisa, Assistência Técnica e Extensão Rural (INCAPER) é responsável
              por...

        - **CEPDEC:**
            - O Centro de Pesquisas de Desastres Climáticos (CEPDEC) concentra seus esforços na pesquisa
              e prevenção de...

        - **ANA:**
            - A Agência Nacional de Águas (ANA) desempenha um papel crucial na gestão dos recursos hídricos
              no Brasil, monitorando...

        - **INMET:**
            - O Instituto Nacional de Meteorologia (INMET) é responsável por coletar e fornecer informações
              meteorológicas para todo o país...

        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
