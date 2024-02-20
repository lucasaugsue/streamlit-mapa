import streamlit as st

def show_sobre():
    st.title("Sobre")

    st.write("""
        ## Sobre o Projeto

        Bem-vindo ao Mapa de Estações Meteorológicas, um projeto que visa fornecer informações
        meteorológicas em tempo real e dados históricos das estações localizadas na região.

        ### Objetivo
        O objetivo deste projeto é oferecer uma visão detalhada das condições meteorológicas
        e fornecer dados úteis para análises e tomada de decisões relacionadas ao clima.

        ### Desenvolvedores
        Este projeto foi desenvolvido por uma equipe dedicada de entusiastas da meteorologia.

        ### Contato
        Para mais informações ou perguntas, entre em contato conosco através do email:
        [lucasaugsue7@gmail.com](mailto:lucasaugsue7@gmail.com)
    """)

def main():
    show_sobre()

if __name__ == "__main__":
    main()