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

@app.route('/index_2')
def index_2():
    return render_template('index_2.html')

@app.route('/index_3')
def index_3():
    return render_template('index_3.html')

@app.route('/index_4')
def index_4():
    return render_template('index_4.html')

@app.route('/portfolio_2')
def portfolio_2():
    return render_template('portfolio_2.html')

@app.route('/portfolio_3')
def portfolio_3():
    return render_template('portfolio_3.html')

@app.route('/portfolio_4')
def portfolio_4():
    return render_template('portfolio_4.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/single_project')
def single_project():
    return render_template('single_project.html')