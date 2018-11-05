from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_login import login_required
from model import db, WorkPleace, Shop
from login import current_user
from passlib.apps import custom_app_context as pwd_context
class User(Resource):
    def get(self):
        query1 = db.session.query(WorkPleace.namePleace, Shop.shopname).join(Shop).order_by(Shop.shopname).all()
        #query1 = query.order_by(Shop.shopname)
        name = ['workplacename', 'shopname']
        l2 = list(dict(zip(name,x)) for x in query1)
        return jsonify(l2)

    #@login_required
    def post(self):
        json_data = request.get_json(force= True)
        shop1 = db.session.query(Shop).filter(Shop.shopname == json_data['shopname']).first()
        createuser = WorkPleace(json_data["username"])
        createuser.hash_password(json_data['pass'])
        db.session.add(createuser)
        shop1.child.append(createuser)
        db.session.commit()
        resp = jsonify(success=True)
        return resp