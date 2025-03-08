from flask import render_template, Blueprint

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/accordion')
def accordion():
    return render_template('main/accordion.html')
@main.route('/check')
def check():
    return render_template('main/check.html')
