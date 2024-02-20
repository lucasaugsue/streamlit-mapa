import streamlit as st

def show_dados_historicos():
    st.title("Dados Históricos")

    st.write("""
        ## Dados Históricos

        Nesta seção, você encontrará uma visão geral dos dados meteorológicos históricos coletados
        pelas estações ao longo do tempo.

        ### Resumo Anual

        - **Ano 2023:**
            - Precipitação média: 1200 mm
            - Temperatura média: 25°C
            - Velocidade média do vento: 10 km/h

        - **Ano 2022:**
            - Precipitação média: 1100 mm
            - Temperatura média: 24°C
            - Velocidade média do vento: 9 km/h

        ### Resumo Mensal

        - **Janeiro 2023:**
            - Precipitação média: 100 mm
            - Temperatura média: 28°C
            - Velocidade média do vento: 12 km/h

        - **Fevereiro 2023:**
            - Precipitação média: 80 mm
            - Temperatura média: 26°C
            - Velocidade média do vento: 11 km/h

        ...

        ### Dados Detalhados

        - Para obter dados detalhados de cada estação, entre em contato conosco.
    """)


def main():
    show_dados_historicos()

if __name__ == "__main__":
    main()