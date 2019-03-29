import datetime
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy.hybrid import hybrid_property
from sqlalchemy import event
from sqlalchemy.event import listen, listens_for
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
# from app import app
db = SQLAlchemy()

class Shop(db.Model):
    __tablename__ = 'shop'
    def __init__(self, shopName):
        self.shopname = shopName
    id = db.Column(db.Integer, primary_key= True)
    shopname = db.Column(db.String(120))    # родительское отношение
    child = db.relationship('WorkPleace', backref='shop', lazy=True)
    def __repr__(self):
        return '<Shop Name %r>' % self.shopname

class WorkPleace(db.Model,UserMixin):
    __tablename__ = 'workpleace'
    id = db.Column(db.Integer, primary_key=True)
    namePleace = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    parent_id = db.Column(db.Integer, db.ForeignKey('shop.id'))# children relationship
    morningdeskchildren = db.relationship("MorningDesk", backref='workpleace')# родительское отношение
    inkasationchildren = db.relationship("Inkasation", backref='workpleace')  # родительское отношение
    eveningreportchildren = db.relationship("EveningReport", backref='workpleace')  # родительское отношение
    rulechildren = db.relationship("PlaceRule", backref='workpleace')  # родительское отношение

    def __init__(self, namePleace):
        self.namePleace = namePleace
        # self.password_hash = self.hash_password(password_hash)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    def __repr__(self):
        return '<Pleace Name %r>' % self.namePleace

class PlaceRule(db.Model,UserMixin):
    __tablename__ = 'rule'
    id = db.Column(db.Integer, primary_key=True)
    rule = db.Column(db.String(120))
    parent_id = db.Column(db.Integer, db.ForeignKey('workpleace.id'))# children relationship

    def __init__(self, rule, pid):
        self.rule = rule
        self.parent_id = pid

    def __repr__(self):
        return '<Rule %r>' % self.rule

class MorningDesk(db.Model):
    __tablename__ = 'morningdesk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desksumm = db.Column(db.Float)
    morningdate = db.Column(db.Date, default=datetime.date.today())

    parent_id = db.Column(db.Integer, db.ForeignKey('workpleace.id'))# children relationship
    suser_label = db.Column(db.Boolean, default=False, nullable=False)
    @hybrid_property
    def isEmpty(self):
        return True if self.morningdate == datetime.date.today() else False
    def __repr__(self):
        return "<morning desk('%s','%s', '%s')>" % (self.id,self.desksumm,self.morningdate)

class Inkasation(db.Model):
    __tablename__ = 'inkasation'
    id = db.Column(db.Integer, primary_key=True)
    transactionSumm = db.Column(db.Float)
    title = db.Column(db.String(120))
    transactiondate = db.Column(db.Date, default=datetime.date.today())

    parent_id = db.Column(db.Integer, db.ForeignKey('workpleace.id'))  # children relationship
    def __init__(self,transactionSumm,title ,transactiondate ):
        self.transactionSumm = transactionSumm
        self.title = title
        self.transactiondate = transactiondate

    def __repr__(self):
        return '<transaction summ( "%s", "%s")>' % (self.transactionSumm, self.title)

class EveningReport(db.Model):
    __tablename__ = 'eveningreport'
    id = db.Column(db.Integer, primary_key=True)
    computerdesk = db.Column(db.Float)
    desk = db.Column(db.Float)
    rozmen = db.Column(db.Float)
    nocashtransaction = db.Column(db.Float)
    reportdate = db.Column(db.Date, default=datetime.date.today())

    parent_id = db.Column(db.Integer, db.ForeignKey('workpleace.id'))  # children relationship

    def __init__(self,computerdesk, desk, rozmen, nocashtransaction, reportdate):
        self.computerdesk = computerdesk
        self.desk = desk
        self.rozmen = rozmen
        self.nocashtransaction = nocashtransaction
        self.reportdate = reportdate

    @staticmethod
    def last():
        return db.session.query(EveningReport.reportdate).order_by(EveningReport.reportdate.desc()).first()[0]

    @staticmethod
    def sevenDayAgo():
        last = EveningReport.last()
        sevenday = last - datetime.timedelta(days=7)
        return sevenday

    @hybrid_property
    def isEmpty(self):
        return True if self.reportdate == datetime.date.today() else False
    def __repr__(self):
        return '<evening report %r>' % self.computerdesk

class Emitent(db.Model):
    __tablename__ = 'emitent'

    def __init__(self, emitent):
        self.emitentname = emitent

    id = db.Column(db.Integer, primary_key=True)
    emitentname = db.Column(db.String(120))

    def __repr__(self):
        return '<emi( "%s", "%s")>' % (self.id, self.emitentname)

@listens_for(WorkPleace, 'after_insert')
def generate_license(*args, **kwargs):
    c = args[2]
    @event.listens_for(db.session, "after_flush", once=True)
    def receive_after_flush(session, context):
        session.add(PlaceRule("USER",c.id ))



