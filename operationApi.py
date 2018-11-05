from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from flask_login import login_required
from model import db, WorkPleace, Inkasation
from sqlalchemy import Date, cast
from datetime import date
from login import current_user
from flask_login import login_required

class Operation(Resource):
    #@login_required
    def get(self):
        incasData = db.session.query(WorkPleace.namePleace,Inkasation.transactionSumm, Inkasation.title).join(Inkasation)
        if request.args.get("day") != None:
            print(request.args.get("day"))
            incasData = incasData.filter(Inkasation.transactiondate == date.today())
        if request.args.get("thisUser") != None:
            print(request.args.get("thisUser"))
            print(current_user.id, "in if its wrong")
            incasData = incasData.filter(WorkPleace.id == current_user.id)
        incasData = incasData.all()
        incasData = list(filter(lambda x: x[1] != None, incasData))
        b = ("placename","sum", "name")
        l1 = list(dict(zip(b,x)) for x in incasData)
        print(l1)
        return jsonify(l1)

    #@login_required
    def post(self):
        json_data = request.get_json(force= True)

        # data = json_data['kashDesk']
        Deskdata = Inkasation(json_data["sum"], json_data["name"])
        db.session.add(Deskdata)
        user1 = db.session.query(WorkPleace).filter_by(namePleace=current_user.namePleace).first()
        user1.inkasationchildren.append(Deskdata)
        db.session.commit()
        resp = jsonify(success=True)
        return resp

# d = [{'sum':200, 'name':'fitolek'}, {'sum':250, 'name':'optima'}]
# @app.route('/operation/', methods=['GET', 'POST'])
# def operation():
#
#     if request.method == 'POST':
#         d.append(request.get_json(force=True))
#         print(d)
#         resp = jsonify(success=True)
#         return resp
#     else:
#         return jsonify(operation=d)
# def postoperation():
#     if request.method == 'POST':
#         print( request.values.get('name'))