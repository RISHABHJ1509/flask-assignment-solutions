#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


conn = sqlite3.connect('items.db', check_same_thread=False)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
conn.commit()

@app.route('/')
def index():
    # Retrieve items from the database
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    return render_template('index1.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    # Add item to the database
    name = request.form['name']
    cursor.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    # Delete item from the database
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
