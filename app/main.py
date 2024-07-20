import streamlit as st
import pandas as pd
from urllib.error import URLError

# URL de l'API exposée via ngrok
API_URL = "https://afba-176-181-170-72.ngrok-free.app"

st.title('API via Streamlit')

table_name = st.text_input('Nom de la table')
start_date = st.text_input('Date de début (YYYY-MM-DD)')
end_date = st.text_input('Date de fin (YYYY-MM-DD)')

if st.button('Obtenir les données'):
    if table_name and start_date and end_date:
        try:
            response = pd.read_json(f"{API_URL}?table_name={table_name}&start_date={start_date}&end_date={end_date}")
            st.write(response)
        except URLError as e:
            st.error(f"Erreur lors de l'appel à l'API: {e}")
        except Exception as e:
            st.error(f"Erreur inattendue: {e}")
    else:
        st.error('Veuillez entrer tous les paramètres.')
