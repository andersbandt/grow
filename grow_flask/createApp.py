from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import abort

import envControl.control.pumpControl as pumpControl



def createApp():
	app = Flask(__name__)

	return app




def routes():
	@app.route('/')
	def index():
		return render_template('index.html',**locals()) # locals are the variables I pass


	@app.route('/pump/', methods=['POST'])
	def pumpControl():
		pumpControl.pumpFluid('acid', 20)
		return render_template('index.html',**locals()) # locals are the variables I pass








	app.debug = True
	app.run()
