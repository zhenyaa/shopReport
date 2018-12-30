from flask_restful import Resource
from flask import request, jsonify
from model.model import db, WorkPleace, MorningDesk, Shop, Inkasation, EveningReport
import datetime
from flask_login import login_required
from additionalFunc import requires_roles

class SuserLabel(Resource):

    @login_required
    @requires_roles("SUPERUSER")
    # def get(self):
    #     query1 = db.session.query(Shop.shopname,WorkPleace.namePleace, MorningDesk.desksumm, db.func.sum(Inkasation.transactionSumm),EveningReport.desk, EveningReport.computerdesk, EveningReport.nocashtransaction, EveningReport.rozmen, EveningReport.reportdate)\
    #         .join(WorkPleace)\
    #         .join(MorningDesk)\
    #         .outerjoin(Inkasation )\
    #         .join(EveningReport) \
    #         .filter(MorningDesk.morningdate == EveningReport.reportdate) \
    #         .filter(MorningDesk.morningdate == Inkasation.transactiondate) \
    #         .group_by(WorkPleace.namePleace, Inkasation.transactiondate)
    #     if request.args.get("shop") != "null":
    #          query1 = query1.filter(Shop.shopname == (request.args.get("shop")))
    #     if request.args.get("shopDesk") != "null":
    #          query1 = query1.filter(WorkPleace.namePleace == (request.args.get("shopDesk")))
    #     if request.args.get("dateStart") != "null":
    #          date1 = datetime.datetime.strptime(request.args.get("dateStart"), "%a %b %d %Y").date()
    #          date2 = datetime.datetime.strptime(request.args.get("dateEnd"), "%a %b %d %Y").date()
    #          query1 = query1.filter(EveningReport.reportdate.between(date1, date2))
    #     if request.args.get("inctitle") != "null":
    #          query1 = query1.filter(Inkasation.title == (request.args.get("inctitle")))
    #     title = ("shopname", "placename", "morningR", "tsum", "erd", "erc", "ern", "err", "erdate")
    #     result = list(dict(zip(title, x)) for x  in query1.all())
    #     return jsonify(result)
    @login_required
    @requires_roles("SUPERUSER")
    def put(self):
        json_data = request.get_json(force= True)
        if json_data['state'] == True:
            query = db.session.query(MorningDesk).get(json_data['id'])
            query.suser_label = True
            db.session.commit()
        if json_data['state'] == False:
            query = db.session.query(MorningDesk).get(json_data['id'])
            query.suser_label = False
            db.session.commit()
        resp = jsonify(success=True)
        return resp
