from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_worker:[pass]@localhost/simple_chat'
db = SQLAlchemy( app )

class History(db.Model):
      id = db.Column('id', db.Integer, primary_key=True)
      message = db.Column('message', db.String(500))

@socketio.on('message')
def hanleMessage(msg):
    print ('Message: %s' % msg)

    message = History(message=msg)
    db.session.add(message)
    db.session.commit()
    send(msg, broadcast=True)

@app.route('/', methods=['GET'])
def index():
    messages = History.query.all()
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    # app.run(debug=True, port=8081)
    socketio.run(app)
