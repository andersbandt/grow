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

@blueprint.route('/recordEC')
def recordEC():
	sensorControl.readEC()
	return

# light stuff
@blueprint.route('/lightOn')
def lightOn():
	print("The light should be on")
	lightControl.lightOn()
	return render_template('control.html', **locals())

@blueprint.route('/lightOff')
def lightOff():
	print("The light should be off")
	lightControl.lightOff()
	return render_template('control.html', **locals())

# air and water stuff
@blueprint.route('/airOn')
def airOn():
	print("The air pump should be on!")
	airControl.airOn()
	return render_template('control.html', **locals())

@blueprint.route('/airOff')
def airOff():
	print("The air pump should be off!")
	airControl.airOff()
	return render_template('control.html', **locals())

@blueprint.route('/waterOn')
def waterOn():
	waterControl.waterOn()
	print("The main water pump should be on")
	return "Water status: on"

@blueprint.route('/waterOff')
def waterOff():
	print("The water pump should be off!")
	waterControl.waterOff()
	return "water status: off"

# fan stuff
@blueprint.route('/intakeOn')
def intakeOn():
	fanControl.intakeOn()
	print("The intake fan should be on")
	return "Intake status: on"

@blueprint.route('/intakeOff')
def intakeOff():
	fanControl.intakeOff()
	print("The intake fan should be off")
	return "Intake status: off"

@blueprint.route('/outtakeOn')
def outtakeOn():
	fanControl.outtakeOn()
	print("The outtake fan should be on")
	return "Intake status: on"

@blueprint.route('/outtakeOff')
def outtakeOff():
	fanControl.outtakeOff()
	print("The outtake fan should be off")
	return "Intake status: off"


