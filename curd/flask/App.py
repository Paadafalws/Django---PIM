from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def lista_registros():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tabela_exemplo')
    registros = cursor.fetchall()
    conn.close()
    return render_template('lista_registros.html', registros=registros)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_registro():
    if request.method == 'POST':
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tabela_exemplo VALUES (?, ?)',
                       (request.form['campo1'], request.form['campo2']))
        conn.commit()
        conn.close()
        return redirect(url_for('lista_registros'))
    else:
        return render_template('adicionar_registro.html')
    

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar_registro(id):
    if request.method == 'POST':
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE tabela_exemplo SET coluna1 = ?, coluna2 = ? WHERE id = ?',
                       (request.form['campo1'], request.form['campo2'], id))
        conn.commit()
        conn.close()
        return redirect(url_for('lista_registros'))
    else:
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tabela_exemplo WHERE id = ?', (id,))
        registro = cursor.fetchone()
        conn.close()
        return render_template('editar_registro.html', registro=registro)
    
@app.route('/excluir/<id>')
def excluir_registro(id):
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tabela_exemplo WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('lista_registros'))

