from flask import Flask, request, jsonify,  render_template, abort, g, flash, Response, redirect, make_response, send_file, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Resource, Api
from flask import session as sess
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, user_loaded_from_request
from flask_sqlalchemy import SQLAlchemy
from operationApi import Operation
from morningReport import MorningDek
from lastReport import LastReport
from adminReport import AdminReport
from login import Login
from model import db, WorkPleace
from shop import ShopAPI
from user import User
from emitentApi import EmitentAPI
from functools import wraps
from flask_alembic import Alembic
app = Flask(__name__, static_url_path="", template_folder="./otchetfrontend/dist", static_folder="./otchetfrontend/dist")
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
db.init_app(app)
alembic = Alembic()
alembic.init_app(app)

SESSION_COOKIE_SECURE = True
REMEMBER_COOKIE_DURATION = 200

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/#/login"
login_manager.session_protection = 'strong'

@login_manager.unauthorized_handler
def unauthorized():
    print("error login, access deny")
    return redirect(url_for('index'))
# @login_manager.request_loader
# def load_user_from_request(request):
#
#     # first, try to login using the api_key url arg
#     print("requeste loader work")
#     api_key = request.args.get('api_key')
#     if api_key:
#         user = User.query.filter_by(api_key=api_key).first()
#         if user:
#             return user
#
#     # next, try to login using Basic Auth
#     api_key = request.headers.get('Authorization')
#     if api_key:
#         api_key = api_key.replace('Basic ', '', 1)
#         try:
#             api_key = base64.b64decode(api_key)
#         except TypeError:
#             pass
#         user = User.query.filter_by(api_key=api_key).first()
#         if user:
#             return user
#
#     # finally, return None if both methods did not login the user
#     return None
def requires_roles(*roles):
    with app.app_context():
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                if current_user.username not in roles:
                    return "No access",403
                return f(*args, **kwargs)
            return wrapped
        return wrapper

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index',  methods=['GET', 'POST'] )
def index():
    return render_template("index.html")

api.add_resource(Login, '/login/')

api.add_resource(AdminReport, '/admin/')
api.add_resource(Operation, '/operation/')
api.add_resource(MorningDek, '/morning/')
api.add_resource(LastReport, '/lastreport/')
api.add_resource(ShopAPI, '/shop/')
api.add_resource(User, '/user/')
api.add_resource(EmitentAPI, '/emitent/')
toolbar = DebugToolbarExtension(app)

@login_manager.user_loader
def user_loader(username):
    user = db.session.query(WorkPleace).filter_by(id=username).first()
    if user:
        return user
    return None

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    SESSION_COOKIE_SECURE = True
    app.run(host='0.0.0.0', debug=True, use_debugger=True, use_reloader=True)