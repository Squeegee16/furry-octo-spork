#
from flask import  render_template,url_for,redirect,flash,request,jsonify, Blueprint
from website import current_app, db
from website.models import Temprature
from website.main.utils import db_convert, create_graphdata, sanitize
import time,datetime
# from sqlalchemy import desc, asc
import re, time, sys
import threading

main = Blueprint('main', __name__)

@main.route("/", methods = ['GET', 'POST'])

def stats():
	if request.method == 'GET' :
		e = Temprature.query.order_by(-Temprature.eid).first()
		t2 = db_convert(e)

	return render_template('dashboard.html',t = t2)
	
@main.route("/hourly", methods = ['GET'])
def hourly_graph():
	b = Temprature.query.order_by(-Temprature.eid).limit(13).all()
	t = db_convert(b)
	hours_data = create_graphdata(t,0)

	return render_template('hourly.html',plot = hours_data)


@main.route("/daily", methods = ['GET'])
def daily_graph():
	g = Temprature.query.order_by(-Temprature.eid).limit(289).all()
	j = db_convert(g)
	day_data = create_graphdata(j,1)

	return render_template('daily.html',plot = day_data)

@main.route("/weekly", methods = ['GET', 'POST'])

def weekly_graph():
	g1 = Temprature.query.order_by(-Temprature.eid).limit(2023).all()
	j1 = db_convert(g1)
	day_data1 = create_graphdata(j1,2)

	return render_template('weekly.html',plot = day_data1)

@main.route("/monthly", methods = ['GET', 'POST'])

def monthly_graph():
	g2 = Temprature.query.order_by(-Temprature.eid).limit(8641).all()
	j2 = db_convert(g2)
	day_data2 = create_graphdata(j2,3)

	return render_template('monthly.html',plot = day_data2)

@main.route("/yearly", methods = ['GET', 'POST'])
def yearly_graph():
	g3 = Temprature.query.order_by(-Temprature.eid).limit(105121).all()
	j3 = db_convert(g3)
	day_data3 = create_graphdata(j3,4)
	return render_template('yearly.html',plot = day_data3)

@main.route("/sanitize")
def san():
		sanitize()
		flash(f'Data Base clean','info')
		return redirect(url_for('main.stats'))
		# return render_template('loc.html')

@main.route("/clean", methods = ['GET'])
def clean():
	# if request.method == 'GET' :

	return render_template('clean.html')