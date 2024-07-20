import streamlit as st
import pandas as pd

# Interface Streamlit
st.title('API via Streamlit')

table_name = st.text_input('Nom de la table')
start_date = st.text_input('Date de début (YYYY-MM-DD)')
end_date = st.text_input('Date de fin (YYYY-MM-DD)')

if st.button('Obtenir les données'):
    if table_name and start_date and end_date:
        try:
            response = pd.read_json(f"http://176.181.170.72:5003/data?table_name={table_name}&start_date={start_date}&end_date={end_date}")
            st.write(response)
        except Exception as e:
            st.error(f"Erreur lors de l'appel à l'API: {e}")
    else:
        st.error('Veuillez entrer tous les paramètres.')
