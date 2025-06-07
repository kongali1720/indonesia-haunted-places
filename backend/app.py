from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Biar frontend bisa ambil data

def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/places', methods=['GET'])
def get_places():
    conn = get_db_connection()
    places = conn.execute('SELECT * FROM haunted_places').fetchall()
    conn.close()

    return jsonify([dict(place) for place in places])

if __name__ == '__main__':
    app.run(debug=True)
