from flask_restful import Resource
from flask import request, jsonify
from model import db, WorkPleace, Inkasation
from datetime import date
from login import current_user
from flask_login import login_required
from additionalFunc import requires_roles

class Operation(Resource):
    @login_required
    @requires_roles("SUPERUSER", "USER")
    def get(self):
        incasData = db.session.query(WorkPleace.namePleace,Inkasation.transactionSumm, Inkasation.title).join(Inkasation)
        if request.args.get("day") != None:
            incasData = incasData.filter(Inkasation.transactiondate == date.today())
        if request.args.get("thisUser") != None:
            incasData = incasData.filter(WorkPleace.id == current_user.id)
        incasData = incasData.all()
        incasData = list(filter(lambda x: x[1] != None, incasData))
        b = ("placename","sum", "name")
        l1 = list(dict(zip(b,x)) for x in incasData)
        return jsonify(l1)

    @login_required
    @requires_roles("SUPERUSER", "USER")
    def post(self):
        json_data = request.get_json(force= True)
        Deskdata = Inkasation(json_data["sum"], json_data["name"])
        db.session.add(Deskdata)
        user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        user1.inkasationchildren.append(Deskdata)
        db.session.commit()
        resp = jsonify(success=True)
        return resp
