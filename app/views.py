from flask import render_template, flash, redirect, session, url_for, request, jsonify, g
from flask.ext.sqlalchemy import get_debug_queries
from app import app, db
from config import DATABASE_QUERY_TIMEOUT


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

