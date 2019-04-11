from flask_restful import Resource
from flask import request, jsonify
from model.model import db, WorkPleace, MorningDesk, Shop, Inkasation, EveningReport
import datetime
from flask_login import login_required
from additionalFunc import requires_roles
class AdminReport(Resource):

    @login_required
    @requires_roles("SUPERUSER")
    def get(self):
        query1 = db.session.query(
            Shop.shopname,
            WorkPleace.namePleace,
            MorningDesk.id,
            MorningDesk.suser_label,
            MorningDesk.desksumm,
            db.func.sum(Inkasation.transactionSumm),
            EveningReport.desk,
            EveningReport.computerdesk,
            EveningReport.nocashtransaction,
            EveningReport.rozmen,
            EveningReport.rro,
            EveningReport.reportdate)\
            .join(WorkPleace)\
            .join(MorningDesk)\
            .outerjoin(Inkasation )\
            .join(EveningReport) \
            .filter(MorningDesk.morningdate == EveningReport.reportdate) \
            .filter(MorningDesk.morningdate == Inkasation.transactiondate) \
            .group_by(WorkPleace.namePleace, Inkasation.transactiondate)
        if request.args.get("shop") != "null":
             query1 = query1.filter(Shop.shopname == (request.args.get("shop")))
        if request.args.get("shopDesk") != "null":
             query1 = query1.filter(WorkPleace.namePleace == (request.args.get("shopDesk")))
        if request.args.get("dateStart") != "null":
             date1 = datetime.datetime.strptime(request.args.get("dateStart"), "%a %b %d %Y").date()
             date2 = datetime.datetime.strptime(request.args.get("dateEnd"), "%a %b %d %Y").date()
             query1 = query1.filter(EveningReport.reportdate.between(date1, date2))
        if request.args.get("inctitle") != "null":
             query1 = query1.filter(Inkasation.title == (request.args.get("inctitle")))
        title = ("shopname", "placename","Mid","Mstate", "morningR", "tsum", "erd", "erc", "ern", "err","rro", "erdate")
        result = list(dict(zip(title, x)) for x  in query1.all())
        return jsonify(result)

    # def post(self):
    #     json_data = request.get_json(force= True)
    #     print(json_data)
    #     resp = jsonify(success=True)
    #     return resp
