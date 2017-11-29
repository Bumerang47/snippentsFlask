from flask import Blueprint, render_template

mod = Blueprint('admin', __name__, template_folder='templates')


@mod.route('/')
def homepage():
    """
    Get template admin page
    @return: admin index.html
    """
    return render_template('admin/index.html')
