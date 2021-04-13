from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',**locals()) # locals are the variables I pass

@app.route('/pump')
def pumpControl():
	return True





if __name__ == '__main__':
	app.debug = True
	app.run()
