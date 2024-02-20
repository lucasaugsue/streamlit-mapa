import folium
import streamlit_folium as stf

def get_pin_color(name_institute):
    color_mapping = {
        "INCAPER": "green",
        "CEPDEC": "orange",
        "ANA": "blue",
        "INMET": "red",
    }
    
    return color_mapping.get(name_institute, "gray")

def create_map(filtered_data):
    # Criando um mapa com Folium
    map_obj = folium.Map(location=[filtered_data[0]['latitude'], filtered_data[0]['longitude']], zoom_start=10)

    # Adicionando marcadores para cada estação no mapa
    for station in filtered_data:
        lat, lon = float(station['latitude']), float(station['longitude'])
        popup_text = f"Nome: {station['name']}\nCódigo: {station['code']}\nTipo: {station['type']}"
        
        # Obtendo a cor do pin com base no nome do instituto
        pin_color = get_pin_color(station['name_institute'])
        
        folium.Marker([lat, lon], popup=popup_text, icon=folium.Icon(color=pin_color)).add_to(map_obj)

    return map_obj

def display_map(filtered_data):
    # Exibindo o mapa no Streamlit usando st_folium
    st_folium = stf.st_folium(create_map(filtered_data))
    st_folium
