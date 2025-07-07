from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

db_path = 'database/veneto_case.db'

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "<h1>Benvenuto nell'API Case Non Occupate - Veneto</h1>"

@app.route('/case', methods=['GET'])
def get_case():
    comune = request.args.get('comune')
    provincia = request.args.get('provincia')

    query = "SELECT * FROM case"
    params = []

    if comune:
        query += " WHERE comune = ?"
        params.append(comune)
    elif provincia:
        query += " WHERE provincia = ?"
        params.append(provincia)

    conn = get_db_connection()
    case = conn.execute(query, params).fetchall()
    conn.close()

    result = [dict(row) for row in case]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
