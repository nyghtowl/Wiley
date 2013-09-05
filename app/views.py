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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio_3')
def portfolio_3():
    return render_template('portfolio_3.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# Support Docs & Test
@app.route('/services2')
def services2():
    return render_template('services2.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog_post')
def blog_post():
    return render_template('blog_post.html')


@app.route('/shortcodes')
def shortcodes():
    return render_template('shortcodes.html')

@app.route('/sidebar_left')
def sidebar_left():
    return render_template('sidebar_left.html')

@app.route('/sidebar_right')
def sidebar_right():
    return render_template('sidebar_right.html')

@app.route('/single_project')
def single_project():
    return render_template('single_project.html')
