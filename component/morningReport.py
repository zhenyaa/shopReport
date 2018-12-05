from flask import request, jsonify
import datetime
import json
from flask_restful import Resource
from flask_login import login_required
from model.model import db, WorkPleace, MorningDesk, Inkasation
from component.login import current_user
from additionalFunc import requires_roles
class MorningDek(Resource):
    # def get(self):
    #     return {'hello': 'world'}

    @login_required
    @requires_roles("USER", "SUPERUSER")
    def post(self):
        emptydata = Inkasation(None,None,datetime.date.today())
        db.session.add(emptydata)
        json_data = request.get_json(force= True)
        data = json_data['kashDesk']
        Deskdata = MorningDesk(desksumm= data, morningdate = datetime.date.today())
        if db.session.query(MorningDesk.morningdate, MorningDesk.parent_id).filter_by(morningdate=datetime.date.today()).filter_by(parent_id=current_user.id).one_or_none():
             return json.dumps({'success':False}), 409, {'ContentType':'application/json'}
        db.session.add(Deskdata)
        user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        user1.morningdeskchildren.append(Deskdata)
        user1.inkasationchildren.append(emptydata)
        db.session.commit()
        resp = jsonify(success=True)
        return resp