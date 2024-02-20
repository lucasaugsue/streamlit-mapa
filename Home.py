import streamlit as st
from mapa import return_map

def main():
    st.title("Mapa de Estações Meteorológicas")

    return_map()

if __name__ == "__main__":
    main()
