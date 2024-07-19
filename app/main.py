import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Configuration de la base de données
DATABASE_URL = "postgresql://pgadmin:changepassword@192.168.1.91:5433/iapmu?client_encoding=utf8"
engine = create_engine(DATABASE_URL)

# Fonction pour obtenir les données de la base de données
def get_data(table_name, start_date, end_date):
    query = text(f"SELECT * FROM {table_name} WHERE \"dateCourse\" BETWEEN :start_date AND :end_date")
    with engine.connect() as conn:
        result = conn.execute(query, {"start_date": start_date, "end_date": end_date}).fetchall()
    return pd.DataFrame(result)

# Interface utilisateur Streamlit
def main():
    st.title('API via Streamlit')

    table_name = st.text_input('Nom de la table')
    start_date = st.text_input('Date de début (YYYY-MM-DD)')
    end_date = st.text_input('Date de fin (YYYY-MM-DD)')

    if st.button('Obtenir les données'):
        if table_name and start_date and end_date:
            data = get_data(table_name, start_date, end_date)
            st.write(data)
        else:
            st.error('Veuillez entrer tous les paramètres.')

# Endpoint API
def api():
    st.title('API Endpoint')
    query_params = st.experimental_get_query_params()
    table_name = query_params.get('table_name', [None])[0]
    start_date = query_params.get('start_date', [None])[0]
    end_date = query_params.get('end_date', [None])[0]

    if table_name and start_date and end_date:
        data = get_data(table_name, start_date, end_date)
        st.json({"data": data.to_dict(orient='records')})
    else:
        st.json({"error": "Missing parameters"})

# Sélection du mode
query_params = st.experimental_get_query_params()
if 'api' in query_params:
    api()
else:
    main()