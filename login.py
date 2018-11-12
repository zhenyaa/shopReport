from flask_restful import Resource
from flask import request, g, jsonify
from flask import session as sess
from flask_login import login_user, logout_user, login_required, current_user
from model import db, WorkPleace
import json
from additionalFunc import requires_roles

def getRole(obj):
    return obj.rulechildren[0].rule

def checkTrue(arrey):
    arrey = tuple(arrey)
    if True in arrey:
        return True
    else:
        return False

class Login(Resource):
    # def get(self):
    #     print("LOGOUT G.USER", g)
    #     logout_user()
    #     return redirect('index')
    #     return (401)

    def post(self):
        if 'user_id' not in sess:
            if "name" and "pass" in request.get_json(force=True):
                UserLogin = request.get_json(force=True)
                username = UserLogin['name']
                password = UserLogin['pass']
                user = db.session.query(WorkPleace).filter_by(namePleace=username).first()
                if not user or not user.verify_password(password):
                    return jsonify(success=False)
                else:
                        login_user(user)
                        user.is_authenticated
                        g.user =  current_user
                        test1 = map(lambda x : True if x.isEmpty == True else False,current_user.morningdeskchildren )
                        test3 = map(lambda x : True if x.isEmpty == True else False, current_user.eveningreportchildren)
                        # print(current_user.rulechildren[0].rule)
                        return json.dumps({'success': True, 'rule':current_user.rulechildren[0].rule, "m": checkTrue(test1), "e": checkTrue(test3)}), 200, {'ContentType': 'application/json'}
        resp = jsonify(success=False)
        return resp

    @login_required
    @requires_roles("ALL","USER", "SUPERUSER")
    def delete(self):
        print("LOGOUT G.USER", g)
        logout_user()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

