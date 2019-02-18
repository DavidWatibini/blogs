from flask import render_template,url_for
from . import main
from ..request import *

@main.route('/')
def index():

    title = 'Home Page - Welcome to wat Blogs, your daily inspiration'

    
    popular = get_quote('popular')
    
    return render_template('index.html', title=title,popular=popular)
