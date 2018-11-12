from flask_restful import Resource
from flask import request, jsonify
from model import db, Emitent
from flask_login import login_required
from additionalFunc import requires_roles
class EmitentAPI(Resource):

    @login_required
    @requires_roles("USER", "SUPERUSER")
    def get(self):
        emitent1 = db.session.query(Emitent.id, Emitent.emitentname).all()
        shablon = ("id", "name")
        result = list(dict(zip(shablon, x)) for x in emitent1)
        return jsonify(result)

    @login_required
    @requires_roles("SUPERUSER")
    def post(self):
        json_data = request.get_json(force=True)
        emi = Emitent(json_data['name'])
        db.session.add(emi)
        db.session.commit()
        resp = jsonify(success=True)
        return resp