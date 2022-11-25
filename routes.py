from finance_track import apps
from flask import render_template, session


@apps.route('')
def index():
    if 'role' in session:
        session.pop('role', None)
    return render_template('index.html')
