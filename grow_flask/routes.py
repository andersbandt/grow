from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import abort
from flask.blueprints import Blueprint


blueprint = Blueprint('routes', __name__, template_folder='/templates')


@blueprint.route('/')
def home():
	return render_template('index.html',**locals()) # locals are the variables I pass

