import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'hey lil momma lemme whithper in yer ear'
messages = []


def add_message(username, message):
    """add messages to the messages list"""
    now = datetime.now().strftime('%H:%M:%S')
    messages.append({'timestamp': now, "from": username, "message": message})


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
    if 'username' in session:
        return redirect(url_for('user', username=session['username']))
    """ Main page with instructions """
    return render_template('index.html')


@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    """display chat messages"""

    if request.method == 'POST':
        username = session['username']
        message = request.form['message']
        add_message(username, message)
        return redirect(url_for('user', username=session['username']))

    return render_template('chat.html', username=username,
                           chat_messages=messages)


@app.route('/<username>/<message>')
def sendmessage(username, message):
    """create a new message and redirect to chat page"""
    add_message(username, message)
    return redirect('/' + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
