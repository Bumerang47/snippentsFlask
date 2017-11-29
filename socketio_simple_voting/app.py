from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_worker:[pass]@localhost/voting'
db = SQLAlchemy( app )

class Results(db.Model):
      id = db.Column('id', db.Integer, primary_key=True)
      vote = db.Column('data', db.Integer)

@socketio.on('vote')
def hanleVote(ballot):
    vote = Results(vote=ballot)

    db.session.add(vote)
    db.session.commit()
    results1 = Results.query.filter_by(vote=1).count()
    results2 = Results.query.filter_by(vote=2).count()

    emit('vote_results', {'results1': results1, 'results2': results2}, broadcast=True)

@app.route('/', methods=['GET'])
def index():
    # messages = History.query.all()
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(debug=True, port=8081)
    socketio.run(app, port=8081)
