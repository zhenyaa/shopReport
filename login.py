from flask_restful import Resource, Api
from flask import Flask, request, g, jsonify, redirect
from flask import session as sess
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from model import db, WorkPleace, MorningDesk, EveningReport
import json
from datetime import date
# from app import db as dbLogin
#from model import WorkPleace

# def requires_roles(*roles):
#     def wrapper(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             if current_user.username not in roles:
#                 return "No access",403
#             return f(*args, **kwargs)
#         return wrapped
#     return wrapper

# @login_manager.user_loader
# def user_loader(username):
#     user = dbLogin.session.query(SellerUser).filter_by(id=username).first()
#     if user:
#         return user
#     return None

def checkTrue(arrey):
    # print("wotch arryy", set(arrey))
    arrey = tuple(arrey)
    #print(arrey)
    if True in arrey:
        return True
    else:
        return False

class Login(Resource):
    def get(self):
        print("LOGOUT G.USER", g)
        logout_user()
        return redirect('index')
        return (401)

    def post(self):
        if 'user_id' not in sess:
            if "name" and "pass" in request.get_json(force=True):
                UserLogin = request.get_json(force=True)
                username = UserLogin['name']
                password = UserLogin['pass']
                user = db.session.query(WorkPleace).filter_by(namePleace=username).first()
                if not user or not user.verify_password(password):
                    return redirect('/')
                else:
                        login_user(user)
                        user.is_authenticated
                        g.user =  current_user
                        test1 = map(lambda x : True if x.isEmpty == True else False,current_user.morningdeskchildren )
                        test3 = map(lambda x : True if x.isEmpty == True else False, current_user.eveningreportchildren)
                        if current_user.id == 1:
                            return json.dumps({'success': True, 'rule': "1", "m": checkTrue(test1), "e": checkTrue(test3)}), 200, {'ContentType': 'application/json'}
                        else:
                            return json.dumps({'success':True, 'rule': "3"}), 200, {'ContentType':'application/json'}
        resp = jsonify(success=False)
        return resp

    def delete(self):
        #print(user)
        print("LOGOUT G.USER", g)
        logout_user()
        #return redirect('index')
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}



    #   if 'user_id' not in sess:
    #       #if "Username" and "Password" in request.form:
    #       if "name" and "pass" in request.get_json(force = True):
    #           UserLogin = request.get_json(force = True)
    #           username = UserLogin['name']
    #           password = UserLogin['pass']
    #           user = session.query(SellerUser).filter_by(username=username).first()
    #           if not user or not user.verify_password(password):
    #               return redirect('/')
    #           else:
    #               login_user(user)
    #               user.is_authenticated
    #               g.user =  current_user
    #               return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    #           return " "
    #       print("loged not in session")
    #   print(sess)
    # return render_template("index.html")