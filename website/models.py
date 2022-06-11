from website import db
from flask import current_app
# from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql import func
from datetime import datetime

class Temprature(db.Model):
    __tablename__ = 'Temprature'
    eid = db.Column(db.Integer, primary_key=True,nullable = True)
    date_stamp = db.Column(db.String(27),unique = False,nullable = True)
    year = db.Column(db.String(4),unique = False,nullable = True)
    mon = db.Column(db.String(2),unique = False,nullable = True)
    day = db.Column(db.String(2),unique = False,nullable = True)
    tod = db.Column(db.String(8),unique = False,nullable = True)
    hour = db.Column(db.String(2),unique = False,nullable = True)
    minute = db.Column(db.String(2),unique = False,nullable = True)
    temp = db.Column(db.Float,unique = False, nullable = True)

    def __repr__(self):
        return f"Temprature('{self.eid}','{self.date_stamp}','{self.year}','{self.mon}','{self.day}','{self.tod}','{self.hour}','{self.minute}','{self.temp}')"