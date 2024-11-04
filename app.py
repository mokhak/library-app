from flask import Flask, request, jsonify
from service import BookService
from models import Schema

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Welcome to Kirat's Library!"

@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(BookService().list_books())

@app.route("/books", methods=["POST"])
def create_book():
    return jsonify(BookService().create_book(request.get_json()))

@app.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    return jsonify(BookService().get_book_by_id(book_id))

@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    return jsonify(BookService().update_book(book_id, request.get_json()))

@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    return jsonify(BookService().delete_book(book_id))

if __name__ == "__main__":
    Schema()
    app.run(host='0.0.0.0', port=8080, debug=True)