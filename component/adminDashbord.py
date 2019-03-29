from flask_restful import Resource, fields, marshal_with
from flask import request, jsonify
from model.model import db, WorkPleace, MorningDesk, Shop, Inkasation, EveningReport
import datetime
from flask_login import login_required
from additionalFunc import requires_roles

resource_fields = {
    'name': fields.String,
    'summ': fields.String,
}

class Dashbord(Resource):
    def get(self, typeD):

        if typeD == "summ":
            query1 = db.session.query( db.func.sum(EveningReport.desk)).filter(EveningReport.reportdate.between(EveningReport.sevenDayAgo(), EveningReport.last())).all()
            return {'summ': query1[0][0]}

        elif typeD == "incs":
            query2 = db.session.query(db.func.sum(Inkasation.transactionSumm)).filter(Inkasation.transactiondate.between(EveningReport.sevenDayAgo(), EveningReport.last())).all()
            return {"incsumm": query2[0][0]}

        elif typeD == "rad":
            query3 = db.session.query(Shop.shopname, db.func.sum(EveningReport.desk)).join(WorkPleace, EveningReport).filter(EveningReport.reportdate.between(EveningReport.sevenDayAgo(), EveningReport.last())).group_by(Shop.shopname).all()
            shablon = ("name", "sum")
            result = list(dict(zip(shablon, x)) for x in query3)
            return jsonify(result)
        elif typeD == "chart":
            shablon = ("name", "sum")
            query4 = db.session.query(Shop.shopname, EveningReport.desk, EveningReport.reportdate).join(WorkPleace, EveningReport).filter(EveningReport.reportdate.between(EveningReport.sevenDayAgo(), EveningReport.last())).all()
            l = list()
            datelist = list()
            outl = list()
            wordName = ""
            for i, c, dt in query4:
                print(i, c)
                if not wordName:
                    wordName = i
                    l.append(c)
                    # print(type(dt))
                    if dt.strftime("%A") not in datelist:
                        datelist.append(dt.strftime("%A"))
                elif wordName == i:
                    l.append(c)
                    if dt.strftime("%A") not in datelist:
                        datelist.append(dt.strftime("%A"))
                elif wordName != i:
                    outl.append({"data": l, "label": wordName})
                    wordName = i
                    if dt.strftime("%A") not in datelist:
                        datelist.append(dt.strftime("%A"))
                    l= list()
                    l.append(c)
            outl.append({"data": l, "label": wordName})
            # outl.append({"listday": datelist})
            out2 = {"point": outl, "day": datelist }
            print(out2)
            return jsonify(out2)






            return {"ok": 200,}
        print(typeD)
        return {'ok': 200,}
