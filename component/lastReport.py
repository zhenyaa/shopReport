from flask_restful import Resource
from flask import request, jsonify
from model.model import db, WorkPleace, EveningReport, Inkasation
from component.login import current_user
from additionalFunc import requires_roles
from flask_login import login_required
import json
import datetime
class LastReport(Resource):
    # def get(self):
    #     return {'hello': 'world'}
    @login_required
    @requires_roles("USER", "SUPERUSER")
    def post(self):
        emptydata = Inkasation(None, None)
        db.session.add(emptydata)
        json_data = request.get_json(force= True)
        print(json_data)
        Deskdata = EveningReport(json_data["computerDesk"],json_data["desk"],json_data["liveMany"],json_data["notMany"] )
        if db.session.query(EveningReport.reportdate, EveningReport.parent_id).filter_by(reportdate=datetime.date.today()).filter_by(parent_id=current_user.id).one_or_none():
            return json.dumps({'success': False}), 409, {'ContentType': 'application/json'}
        db.session.add(Deskdata)
        user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        user1.eveningreportchildren.append(Deskdata)
        user1.inkasationchildren.append(emptydata)
        db.session.commit()
        resp = jsonify(success=True)
        return resp