from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_login import login_required
from model import db, WorkPleace, Shop
from login import current_user
class ShopAPI(Resource):
    def get(self):
        shop1 = db.session.query(Shop.shopname).all()
        l1 = list({'shopname':x[0]} for x in shop1)
        return jsonify(l1)

    @login_required
    def post(self):
        json_data = request.get_json(force= True)
        print(json_data)
        shopname = json_data['name']
        newShop = Shop(shopname)
        db.session.add(newShop)
        db.session.commit()
        # data = json_data['kashDesk']
        # Deskdata = MorningDesk(desksumm= data)
        # db.session.add(Deskdata)
        # user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        # user1.morningdeskchildren.append(Deskdata)
        # db.session.commit()
        resp = jsonify(success=True)
        return resp