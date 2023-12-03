from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, request
from flask import session as Session
from flask_bootstrap import Bootstrap

from functools import wraps
from datetime import timedelta

from app.config import CONFIG

app = Flask(__name__)
Bootstrap(app)
app.secret_key = CONFIG['secret_key']
app.permanent_session_lifetime = timedelta(hours=1)


if __name__ == "__main__":
    app.run(host='0.0.0.0')