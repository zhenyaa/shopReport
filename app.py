from flask import Flask, render_template, g, redirect, url_for, current_app
from flask_restful import  Api
from flask_login import LoginManager, current_user
from component.operationApi import Operation
from component.morningReport import MorningDek
from component.lastReport import LastReport
from component.adminReport import AdminReport
from component.login import Login
from model.model import db, WorkPleace
from component.shop import ShopAPI
from component.user import User
from component.emitentApi import EmitentAPI
from component.directorExecuteMoney import ExecuteMoney
from flask_alembic import Alembic
import config
import pymysql
pymysql.install_as_MySQLdb()
app = Flask(__name__, static_url_path="", template_folder="./otchetfrontend/dist", static_folder="./otchetfrontend/dist")
app.config.from_object(config.Development)

api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12358134@localhost/report'
# db = SQLAlchemy(app)
db.init_app(app)
alembic = Alembic()
alembic.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/#/login"
login_manager.session_protection = 'strong'

@login_manager.unauthorized_handler
def unauthorized():
    print(current_user, current_app)
    print("error login, access deny")
    return redirect(url_for('index'))

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
api.add_resource(ExecuteMoney, '/executemoney/')

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
    app.run()