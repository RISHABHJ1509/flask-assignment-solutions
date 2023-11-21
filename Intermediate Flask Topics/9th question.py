#9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for storing books (replace this with a real database)
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'}
]
next_id = 3

# API endpoints
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    global next_id
    data = request.json
    new_book = {'id': next_id, 'title': data['title'], 'author': data['author']}
    books.append(new_book)
    next_id += 1
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.json
        book['title'] = data['title']
        book['author'] = data['author']
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
