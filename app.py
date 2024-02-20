import streamlit as st
import requests
from mapa import display_map

def main():
    st.title("Mapa de Estações Meteorológicas")

    api_url = "http://54.159.5.19:3000/stations"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        all_institutes = sorted(set(station['name_institute'] for station in data))
        selected_institutes = st.sidebar.multiselect("Selecione os Institutos", all_institutes, default=all_institutes)

        filtered_data = [station for station in data if station['name_institute'] in selected_institutes]

        if filtered_data:
            # Chamando a função do mapa para exibir no Streamlit
            display_map(filtered_data)
        else:
            st.warning("Nenhuma estação encontrada para os institutos selecionados.")

    else:
        st.error(f"Falha ao carregar dados da API. Código de status: {response.status_code}")

if __name__ == "__main__":
    main()
