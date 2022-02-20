import os
import redis
from flask import Flask, session, redirect, escape, request

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', default=None)

# BEGIN NEW CODE - PART 1 #
REDIS_URL = os.environ.get('REDIS_URL')
store = redis.Redis.from_url(REDIS_URL)


# END NEW CODE - PART 1 #

@app.route('/')
def index():
    if 'username' in session:
        # BEGIN NEW CODE - PART 2 #
        username = escape(session['username'])
        visits = store.hincrby(username, 'visits', 1)

    return '''
        Logged in as {0}.<br>
        Visits: {1}
        '''.format(username, visits)
    # END NEW CODE - PART 2 #

    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/')

    return '''
        <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>'''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')
