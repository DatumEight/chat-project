import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session 

app = Flask(__name__)
app.secret_key = 'hey lil momma lemme whithper in yer ear'
messages = []


def add_messages(username, message):
    """add messages to the messages list"""
    now = datetime.now().strftime('%H:%M:%S')
    messages.append('({}) {}: {}'.format(now, username, message))


def get_all_messages():
    '''gets all messages'''
    return '<br>'.join(messages)


@app.route('/')
def index():
    """ Main page with instructions """
    return render_template('templates/index.html')


@app.route('/<username>')
def user(username):
    """display chat messages"""
    return "<h1>Welcome, {0} </h1> {1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def sendmessage(username, message):
    """create a new message and redirect to chat page"""
    add_messages(username, message)
    return redirect('/' + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
