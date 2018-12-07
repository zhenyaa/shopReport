from flask_restful import Resource
from flask import request, jsonify
from model.model import db, Emitent, Shop, WorkPleace, Inkasation
from flask_login import login_required
from additionalFunc import requires_roles


class ExecuteMoney(Resource):

    @login_required
    @requires_roles("SUPERUSER")
    def get(self):
        param = "Нехаинко"
        exec = db.session.query(Shop.id, WorkPleace.id, Inkasation.transactiondate).join(WorkPleace).join(Inkasation).filter(Inkasation.title == param).all()
        print(exec)
        shablon = ("Sid", "Wid", "Idate")
        result = list(dict(zip(shablon, x)) for x in exec)
        return jsonify(result)

    # @login_required
    # @requires_roles("SUPERUSER")
    # def post(self):
    #     json_data = request.get_json(force=True)
    #     emi = Emitent(json_data['name'])
    #     db.session.add(emi)
    #     db.session.commit()
    #     resp = jsonify(success=True)
    #     return resp