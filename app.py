from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
db = SQLAlchemy(app)

class customers(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Age = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.ID

# @app.route('/')
# def index():
#     return "<h1 style= 'color: red'>hello flask</h1>"

@app.route('/', methods = ['GET'])
def index():
    my_customers = customers.query.all()
    return render_template('index.html', my_customers=my_customers)



if __name__ == "__main__":
    app.run(host='127.0.0.6', port=8080, debug=True)
