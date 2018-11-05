from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from model import db, WorkPleace, EveningReport, Inkasation, Emitent
from login import current_user
from flask_login import login_required

class EmitentAPI(Resource):
    def get(self):
        emitent1 = db.session.query(Emitent.id, Emitent.emitentname).all()
        shablon = ("id", "name")
        result = list(dict(zip(shablon, x)) for x in emitent1)
        print(result)
        return jsonify(result)

    def post(self):
        json_data = request.get_json(force=True)
        emi = Emitent(json_data['name'])
        db.session.add(emi)
        db.session.commit()
        resp = jsonify(success=True)
        return resp