from flask import request, jsonify
from flask_restful import Resource
from flask_login import login_required
from model.model import db, Shop
from additionalFunc import requires_roles

class ShopAPI(Resource):
    @login_required
    @requires_roles("USER", "SUPERUSER")
    def get(self):
        shop1 = db.session.query(Shop.shopname).all()
        l1 = list({'shopname':x[0]} for x in shop1)
        return jsonify(l1)

    @login_required
    @requires_roles("USER", "SUPERUSER")
    def post(self):
        json_data = request.get_json(force= True)
        print(json_data)
        shopname = json_data['name']
        newShop = Shop(shopname)
        db.session.add(newShop)
        db.session.commit()
        return jsonify(success=True)
