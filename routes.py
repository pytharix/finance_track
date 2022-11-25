from finance_track import app
from flask import render_template, session


@app.route('/')
def index():
    if 'role' in session:
        session.pop('role', None)
    return render_template('index.html')
