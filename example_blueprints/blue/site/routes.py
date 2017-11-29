from flask import Blueprint, render_template

mod = Blueprint('site', __name__, template_folder='templates')


@mod.route('/')
def homepage():
    """
    Get home page
    @return: home index.html
    """
    return render_template('site/index.html')
