from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import abort
from flask.blueprints import Blueprint

from envControl.control import pHControl
from envControl.control import lightControl
from envControl.control import fanControl
from envControl.control import pumpControl
from envControl.control import airControl
from envControl.control import waterControl
from envControl.control import sensorControl

blueprint = Blueprint('routes', __name__, static_folder='static', template_folder='/templates')

@blueprint.route('/')
def home():
	return render_template('index.html',**locals()) # locals are the variables I pass

@blueprint.route('/index.html')
def index_return():
	return home()

@blueprint.route('/automate.html')
def automate():
	return render_template('automate.html')

@blueprint.route('/control.html')
def control():
	return render_template('control.html', **locals())

@blueprint.route('/recordpH')
def recordPH():
	sensorControl.readpH()
	return

@blueprint.route('/lightOn')
def lightOn():
	print("The light should be on")
	lightControl.lightOn()
	return "Light status: on"

@blueprint.route('/lightOff')
def lightOff():
	print("The light should be off")
	lightControl.lightOff()
	return "Light status: off"

@blueprint.route('/airOn')
def airOn():
	print("The air pump should be on!")
	airControl.airOn()
	return "Air status: on"

@blueprint.route('/airOff')
def airOff():
	print("The air pump should be off!")
	airControl.airOff()
	return "Air status: off"

@blueprint.route('/waterOn')
def waterOn():
	waterControl.waterOn()
	return "Water status: on"
