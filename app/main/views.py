from flask import render_template,url_for
from . import main


@main.route('/')
def index():

    title = 'Home Page - Welcome to wat Blogs, your daily inspiration'

    return render_template('index.html', title=title)
