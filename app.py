from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'

db = SQLAlchemy(app)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


@app.route('/')
def home():

    courses = Course.query.all()

    text = ""

    for course in courses:
        text += f"{course.title}<br>"

    return text


@app.route('/add/<title>')
def add(title):

    course = Course(title=title)

    db.session.add(course)
    db.session.commit()

    return "Course Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
