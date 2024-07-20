from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

# Configuration de la base de données
DATABASE_URL = "postgresql+psycopg2://pgadmin:changepassword@176.181.170.72:5433/iapmu?client_encoding=utf8"
engine = create_engine(DATABASE_URL)

# Créer une application Flask
app = Flask(__name__)
@app.route('/data', methods=['GET'])
def get_data():
    table_name = request.args.get('table_name')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not table_name or not start_date or not end_date:
        return jsonify({"error": "Please provide table_name, start_date, and end_date"}), 400

    query = text(f"SELECT * FROM {table_name} WHERE \"dateCourse\" BETWEEN :start_date AND :end_date")
    with engine.connect() as conn:
        result = conn.execute(query, {"start_date": start_date, "end_date": end_date}).fetchall()
    
    data = [dict(row) for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5003, debug=True)