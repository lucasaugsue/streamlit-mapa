import folium
import streamlit_folium as stf
import streamlit as st
import requests

api_url = "http://54.159.5.19:3000/stations"
response = requests.get(api_url)

def get_pin_color(name_institute):
    color_mapping = {
        "INCAPER": "green",
        "CEPDEC": "orange",
        "ANA": "blue",
        "INMET": "red",
    }
    
    return color_mapping.get(name_institute, "gray")

def create_map(filtered_data):
    map_obj = folium.Map(location=[filtered_data[0]['latitude'], filtered_data[0]['longitude']], zoom_start=10)

    for station in filtered_data:
        lat, lon = float(station['latitude']), float(station['longitude'])
        popup_text = f"Nome: {station['name']}\nCódigo: {station['code']}\nTipo: {station['type']}"
        
        pin_color = get_pin_color(station['name_institute'])
        
        folium.Marker([lat, lon], popup=popup_text, icon=folium.Icon(color=pin_color)).add_to(map_obj)

    return map_obj

def display_map(filtered_data):
    # Exibindo o mapa no Streamlit usando st_folium
    st_folium = stf.st_folium(create_map(filtered_data))
    st_folium

def filtro_institutos(data):
    all_institutes = sorted(set(station['name_institute'] for station in data))
    list_filtered = st.sidebar.multiselect("Selecione os institutos", all_institutes, default=all_institutes)
    return list_filtered

def return_map():
    if response.status_code == 200:
        data = response.json()

        selected_institutes = filtro_institutos(data)

        filtered_data = [station for station in data if station['name_institute'] in selected_institutes]

        if filtered_data:
            display_map(filtered_data)
        else:
            st.warning("Nenhuma estação encontrada para os institutos selecionados.")

    else:
        st.error(f"Falha ao carregar dados da API. Código de status: {response.status_code}")
