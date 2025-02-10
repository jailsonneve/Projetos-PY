from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para obter todos os usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conn = get_db_connection()
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return jsonify([dict(usuario) for usuario in usuarios])

# Endpoint para criar um novo usuário
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    new_usuario = request.get_json()
    nome = new_usuario['nome']
    idade = new_usuario['idade']

    conn = get_db_connection()
    conn.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conn.commit()
    conn.close()
    return jsonify(new_usuario), 201

# Inicializando a tabela de usuários no banco de dados
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
