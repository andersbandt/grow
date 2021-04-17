from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import abort
from flask.blueprints import Blueprint

from envControl.control import airControl

blueprint = Blueprint('routes', __name__, static_folder='static', template_folder='/templates')

@blueprint.route('/')
def home():
	return render_template('index.html',**locals()) # locals are the variables I pass


@blueprint.route('/index.html')
def index_return():
	return home()

@blueprint.route('/control.html')
def control():
	return render_template('control.html', **locals())


@blueprint.route('/airOn')
def airOn():
	print("The air pump should be on!")
	airControl.airOn()

@blueprint.route('/airOff')
def airOff():
	print("The air pump should be off!")
	airControl.airOff()


