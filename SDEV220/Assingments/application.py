from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#create a book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

#turn book object into JSON format
    def to_dict(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'author': self.author,
            'publisher': self.publisher
        }
    
#create a book
@app.route('/books', methods=['POST'])
def add_book():
   data= request.get_json()
   new_book = Book(book_name=data.get['book_name'], author=data['author'], publisher=data['publisher'])
   db.session.add(new_book)
   db.session.commit()
   return jsonify(new_book.to_dict()), 201


# read all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])

#update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    db.session.commit()
    return jsonify(book.to_dict())

#home route
@app.route('/')
def home():
    return "Book API Assignment running"

#create the database tables
with app.app_context():
    db.create_all()