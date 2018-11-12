from flask import request, jsonify
from flask_restful import Resource
from flask_login import login_required
from model import db, WorkPleace, MorningDesk, Inkasation
from login import current_user
from additionalFunc import requires_roles
class MorningDek(Resource):
    # def get(self):
    #     return {'hello': 'world'}

    @login_required
    @requires_roles("USER", "SUPERUSER")
    def post(self):
        emptydata = Inkasation(None,None)
        db.session.add(emptydata)
        json_data = request.get_json(force= True)
        data = json_data['kashDesk']
        Deskdata = MorningDesk(desksumm= data)
        db.session.add(Deskdata)
        user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        user1.morningdeskchildren.append(Deskdata)
        user1.inkasationchildren.append(emptydata)
        db.session.commit()
        resp = jsonify(success=True)
        return resp