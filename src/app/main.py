from flask import Flask, session, url_for, redirect, request

# This is a session object. It is nothing more than a dict with some extra methods
from src.app.redis.core import RedisSessionInterface

app = Flask(__name__)
app.session_interface = RedisSessionInterface()


@app.route("/")
def index():
    session.permanent = False
    if not 'refreshed' in session:
        session['refreshed'] = 0

    text = "You refreshed the page %d times" % (session['refreshed'])
    text += '<br/><a href="/kill">Reset</a>'
    text += '<br/>username="%s"' % session.get('username', 'NULL')
    session['refreshed'] = session['refreshed'] + 1
    return text


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        test_u = request.form['username']
        test_p = request.form['username']
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>

    '''


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


app.debug = True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
