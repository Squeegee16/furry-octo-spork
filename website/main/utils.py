import sys
import secrets
from flask import flash #url_for, render_template
from website import current_app,db
from website.models import Temprature
from sqlalchemy.exc import IntegrityError
import re
import math
import datetime, time
import plotly
import plotly.graph_objs as go
import numpy as np
import json

from os import path

def db_convert(data):
	d=[]
	try:
		a = len(data)
		for l in range(a):
			st = '('
			ed = ')'
			D = str(data[l])
			start = D.index(st) + len(st)
			end = D.index(ed, start + 1)
			d.append(re.split(r',',D[start:end]))
		return d

	except TypeError:
		return data.temp

	
def str2int2str(st,tz):

	b = st
	b = int(b.strip('"'))
	a = str(b+tz)
	return a

def strip_(data):# list from database
	f = data.strip('"')
	f = f.strip("'")
	return f

def create_graphdata(list, g_type):
	# ["'444'", "'2022-05-01 10:23:24.930341'", "'2022'", "'05'", "'01'", "'10:23:24'", "'10'", "'23'", "'17.687'"]
	datea = datetime.datetime.now()
	cmonth = int(datea.strftime("%m"))
	data = list
	gtype = g_type
	a = []
	b = []
	for l in range(0,len(list)):
		a.append(data[l][8].strip('"'))

	for i in range(len(a)):
		b.append(float(a[i].strip("'")))

	#gstop = len(list)
	
	
	if gtype == 0: # hourly
		gstop = 13
		h = strip_(data[l][6])
	elif gtype == 1: # daily
		gstop = 289
		d = strip_(data[l][4])
	elif gtype == 2: #week
		gstop = 2023 
		# count days and add date to list
		w = strip_(data[l][1][:11])

	elif gtype == 3:# month
		# count days add to current list#
		#for each day find high's and low's
		gstop = 8641
		m = strip_(data[l][3])
	elif gtype == 4:
		gstop = 105121 #year
		y = strip_(data[l][2])
	else:
		print("Error")

	# Create traces 
	if gtype == 0:
		ytemp = np.asarray(b)
		trace0 = go.Scatter(
			x = np.linspace(0, gstop, gstop),
			y = ytemp,
			name = f'Hour: {h}',
			mode = 'lines', 
			showlegend=True,
			line = {'color': 'rgb(153, 170, 187)', 'width': 3},
			connectgaps= True,
			stackgroup = 'one'
		)
		data = [trace0]

	elif gtype == 1: #hour
		# yd = [ytemp[i:i + 13] for i in range(0, len(ytemp), 13)] 
		ytemp = np.asarray(b)   
		trace0 = go.Scatter(
		x = np.linspace(0, gstop, gstop),
		y = ytemp,
		name = f'Day: {d}',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(153, 170, 187)', 'width': 3},
		connectgaps= True,
		stackgroup = 'one'
		)
		data = [trace0]

	elif gtype == 2:#week 
		ytemp = np.asarray(b)

		res = 289
		
		xd1 = np.linspace(0, 289, res)
		xd2 = np.linspace(290,578,res)
		xd3 = np.linspace(579,868,res)
		xd4 = np.linspace(869,1158,res)
		xd5 = np.linspace(1159,1448,res)
		xd6 = np.linspace(1449,1738,res)
		xd7 = np.linspace(1739,2023,res)

		parameters = [xd1,xd2,xd3,xd4,xd5,xd6,xd7]

		yd = [ytemp[i:i + 289] for i in range(0, len(ytemp), 289)] 

		trace0 = go.Scatter(
		x = xd1,
		y = yd[0],
		name = f'Today',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(128, 0, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'one'
		)

		trace1 = go.Scatter(
		x = xd2,
		y = yd[1],
		name = f'Yesterday',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(255, 69, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'two'
		)

		trace2 = go.Scatter(
		x = xd3,
		y = yd[2],
		name = f'3 Days ago',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(255, 215, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'three'
		)

		trace3 = go.Scatter(
		x = xd4,
		y = yd[3],
		name = f'4 Days ago',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(0, 100, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'four'
		)
  
		trace4 = go.Scatter(
		x = xd5,
		y = yd[4],
		name = f'5 Days ago',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(128, 128, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'five'
		)

		trace5 = go.Scatter(
		x = xd6,
		y = yd[5],
		name = f'6 Days ago',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(70, 130, 180)', 'width': 3},
		connectgaps= True,
		stackgroup = 'six'
		)

		trace6 = go.Scatter(
		x = xd7,
		y = yd[6],
		name = f'7 Days ago',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(139, 0, 139)', 'width': 3},
		connectgaps= True,
		stackgroup = 'seven'
		)

		data = [trace0,trace1,trace2,trace3,trace4,trace5,trace6]

	elif gtype == 3:# month
		# ["'444'", "'2022-05-01 10:23:24.930341'", "'2022'", "'05'", "'01'", "'10:23:24'", "'10'", "'23'", "'17.687'"]
		datea = datetime.datetime.now()
		monNum = int(datea.strftime("%W"))
		d = []
		m= []
		o = {}
		hi = []
		lo = []
		dt = []
		days = []
		mon = []
		for i in range(0, len(list)):
			d.append(strip_(data[i][4]))
			m.append(int(strip_(data[i][3])))
			#day / temp
			dt.append([strip_(data[i][0]),int(strip_(data[i][3])),int(strip_(data[i][4])),float(strip_(data[i][8]))])
		#remove duplicates days
		[days.append(x) for x in d if x not in days]
		[mon.append(x) for x in m if x not in mon]
	   #load unique into dict
		for z in d:
			o[z] = d.count(z)
		# print(o)
		daytemp = []
		#split dictionary
		dai = len(o)+1
		# print(dt)#['2965', 16, 9.5]
		#find current month
		for t in range(0,len(mon)):
			if mon[t] == cmonth:
				print('AAAAA',mon, type(cmonth))
				# find days in month
				for day, cnt in o.items():
					i = 0
					for i in range(0, len(list)):
						print('inside',dt[i][2], dai, i)
						if dt[i][1] == dai:
							
							print('BBBBB',mon, type(cmonth))
							daytemp.append(dt[i][2]) 
						i += 1 
					print('outer',daytemp)   
					hi.append(max(daytemp))
					lo.append(min(daytemp))
					# print(hi, lo)
					dai -= 1
			else: 
				pass

		trace0 = go.Scatter(
		x = days,
		y = hi,
		name = f'Highs',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(255, 0, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'one'
		)

		trace1 = go.Scatter(
		x = days,
		y = lo,
		name = f'Lows',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(0, 0, 255)', 'width': 3},
		connectgaps= True,
		stackgroup = 'two'
		)

		data = [trace0, trace1]

	else:
		datea = datetime.datetime.now()
		dayOyear = int(datea.strftime("%j"))

		d = []
		o = {}
		hi = []
		lo = []
		dt = []
		days = []
# ["'444'", "'2022-05-01 10:23:24.930341'", "'2022'", "'05'", "'01'", "'10:23:24'", "'10'", "'23'", "'17.687'"]
		
		for i in range(0, len(list)):
			d.append(strip_(data[i][4]))
			#day / temp
			dt.append([strip_(data[i][0]),int(strip_(data[i][4])),float(strip_(data[i][8]))])
		#remove duplicates days
		[days.append(x) for x in d if x not in days]
	   #load unique into dict
		for z in d:
			o[z] = d.count(z)
		# print(o)
		yeartemp = []
		#split dictionary
		dai = len(o)+1

		for day, cnt in o.items():
			i = 0
			for i in range(0, len(list)):

				if dt[i][1] == dai:
					# print('inside',dt[i][2], dai, i)
					yeartemp.append(dt[i][2]) 
				i += 1    
			hi.append(max(yeartemp))
			lo.append(min(yeartemp))
			# print(hi, lo)
			dai -= 1

		trace0 = go.Scatter(
		x = days,
		y = hi,
		name = f'Highs',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(255, 0, 0)', 'width': 3},
		connectgaps= True,
		stackgroup = 'one'
		)

		trace1 = go.Scatter(
		x = days,
		y = lo,
		name = f'Lows',
		mode = 'lines', 
		showlegend=True,
		line = {'color': 'rgb(0, 0, 255)', 'width': 3},
		connectgaps= True,
		stackgroup = 'two'
		)
		
		data = [trace0, trace1]



		#ig = go.Figure()

		# fig.add_trace(go.Scatter(
		#     x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
		#     y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
		#     name="Name of Trace 1"       # this sets its legend entry
		# ))

		# fig.update_layout(
		# title={
			# 'text': "Plot Title",
			# 'y':0.9,
			# 'x':0.5,
			# 'xanchor': 'center',
			# 'yanchor': 'top'}),
	    # xaxis_title="X Axis Title",
	    # yaxis_title="Y Axis Title",
	    # legend_title="Legend Title",

	    # font=dict(
	    #     family="Courier New, monospace",
	    #     size=18,
	    #     color="RebeccaPurple"
		#     )
		# )

	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
	
	return graphJSON

def sanitize():
	san_rec = Temprature.query.filter_by(temp = 85.0).all()

	for l in range(len(san_rec)):
		id = san_rec[l].eid
		tu = san_rec[l].eid + 1    
		td = san_rec[l].eid - 1    
		try:
			while True:
				d_up = Temprature.query.filter_by(eid = tu).first()
				
				if d_up.temp == 85:
					tu = tu +1 
				else:
					break

			while True:
				d_down = Temprature.query.filter_by(eid = td).first()
				if d_down.temp == 85:
					td = td -1
				else:
					break

		except TypeError:
			avg = san_rec[l].temp 
			Temprature.query.filter_by(eid = id).update(dict(temp = avg))                   
		
		avg = (d_up.temp + d_down.temp)/2
		Temprature.query.filter_by(eid = id).update(dict(temp = avg))
			
		db.session.commit()
############# not implemented ####################
def dat_tim(request_data,widget_data):#(type:month,month number)
	# ["'444'", "'2022-05-01 10:23:24.930341'", "'2022'", "'05'", "'01'", "'10:23:24'", "'10'", "'23'", "'17.687'"]
	data = request_data
	day={1: 'Sunday',2: 'Monday',3: 'Tuesday',4: 'Wednesday',5: 'Thursday',6: 'Friday',7: 'Saturday'}
	month = {1:'January',2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July' ,8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
	#2022-05-06 11:11:45.615090

	x2 = datetime.datetime.now()
	#month -(8641) start with current one
	b = Temprature.query.order_by(mon = -x2.month).limit(8641).all()

	return data