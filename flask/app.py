from flask import Flask, render_template, url_for,request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__,)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return 'Article %r' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-article')
def create_article():
    if request.method == "POST":
        title = request.form
    else:
        return render_template("create-article")
    




if __name__ == "__main__":
    app.run(debug=True)