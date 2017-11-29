from flask import Flask, request, make_response
from functools import wraps

app = Flask(__name__)


def auth_required(f):
    """
    Wrapper for required authentication [ru] Обертка для проверки на аутентификацию
    @return: decorator function with auth [ru] Функция декоратора с аутентификацией
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated


@app.route('/')
def index():
    """
    First page take basic www-auth [ru] Первая страница принимает базовую web авторизацию
    @return: Authorization response [ru] Ответ авторизации
    """

    if request.authorization and \
       request.authorization.username == 'username' and \
       request.authorization.password == 'password':
        return '<h1>You are logged in</h1>'
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/page')
@auth_required
def page():
    """
    Some privileged page [ru] Некоторая привилигированная страница
    @return: Content page or nothing (404) [ru] Содержимое страницы или ничего (404)
    """

    return '<h1>You are on the page!</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
