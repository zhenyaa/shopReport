from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from model import db, WorkPleace, EveningReport, Inkasation
from login import current_user
class LastReport(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        emptydata = Inkasation(None, None)
        db.session.add(emptydata)
        json_data = request.get_json(force= True)
        print(json_data)
        Deskdata = EveningReport(json_data["computerDesk"],json_data["desk"],json_data["liveMany"],json_data["notMany"] )
        db.session.add(Deskdata)
        user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        user1.eveningreportchildren.append(Deskdata)
        user1.inkasationchildren.append(emptydata)
        db.session.commit()
        resp = jsonify(success=True)
        return resp