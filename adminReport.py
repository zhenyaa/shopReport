from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from model import db, WorkPleace, MorningDesk, Shop, Inkasation, EveningReport
import  datetime
# from app import requires_roles as rqr
from flask_login import login_required

# import app
#from flask_sqlalchemy.sql import func
class AdminReport(Resource):

    @login_required
    def get(self):
        print(request.args.get("shop"))

        # subquery1 = db.session.query(WorkPleace.id.label("idP"),Inkasation.transactiondate.label("idata"), db.func.sum(Inkasation.transactionSumm)).join(Inkasation).group_by(WorkPleace.namePleace, Inkasation.transactiondate)
        # #print(subquery1.all())
        # subquery1.filter(Inkasation.title == "тест1")
        # subquery1 = subquery1.subquery()
        # query1 = db.session.query(Shop.shopname,WorkPleace.namePleace, WorkPleace.id.label("idM"), MorningDesk.desksumm.label("Mds"),EveningReport.desk, EveningReport.computerdesk, EveningReport.nocashtransaction, EveningReport.rozmen, EveningReport.reportdate.label("date")) \
        #     .join(WorkPleace)\
        #     .join(MorningDesk)\
        #     .join(EveningReport)\
        #     .filter(MorningDesk.morningdate == EveningReport.reportdate)
        # if request.args.get("shop") != "null":
        #          query1 = query1.filter(Shop.shopname == (request.args.get("shop")))
        # if request.args.get("shopDesk") != "null":
        #      query1 = query1.filter(WorkPleace.namePleace == (request.args.get("shopDesk")))
        # if request.args.get("dateStart") != "null":
        #      date1 = datetime.datetime.strptime(request.args.get("dateStart"), "%a %b %d %Y").date()
        #      date2 = datetime.datetime.strptime(request.args.get("dateEnd"), "%a %b %d %Y").date()
        #      query1 = query1.filter(EveningReport.reportdate.between(date1, date2))
        #      query1 = query1.subquery()
        # queryRezult = db.session.query(query1, subquery1).filter(query1.c.idM == subquery1.c.idP).filter(query1.c.date == subquery1.c.idata).order_by(query1.c.Mds)
        # #print(queryRezult)
        # # for x in queryRezult:
        # #     print(x)
        # #print(queryRezult.column_descriptions())
        # shablon = ("Shopname", "Workplace", "IDWp", "Mdeck", "Edeck", "Ecdeck", "ENcash", "ER", "Edate", "IDWp2", "SDate", "TSum")
        # a = list(dict(zip(shablon, x)) for x in queryRezult.all())
        # return jsonify(a)


        # param = {"shopname": "apteka1"}
        query1 = db.session.query(Shop.shopname,WorkPleace.namePleace, MorningDesk.desksumm, db.func.sum(Inkasation.transactionSumm),EveningReport.desk, EveningReport.computerdesk, EveningReport.nocashtransaction, EveningReport.rozmen, EveningReport.reportdate)\
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
        for x in query1.all():
            print(x)
        title = ("shopname", "placename", "morningR", "tsum", "erd", "erc", "ern", "err", "erdate")
        result = list(dict(zip(title, x)) for x  in query1.all())
        #print(result)

        return jsonify(result)

    def post(self):
        json_data = request.get_json(force= True)
        print(json_data)
        resp = jsonify(success=True)
        return resp
