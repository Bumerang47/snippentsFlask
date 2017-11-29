from flask import Blueprint

mod = Blueprint('api', __name__)


@mod.route('/getStuff')
def get_stuff():
    """
    Get stuff api
    @return: some material
    """
    return '{"results": "You are in the API!"}'
