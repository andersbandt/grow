from flask import Flask
#import flash
#import redirect
#import render_template
#import request
#import session
#import abort

app = Flask(__name__)

def hello_world():
	return 'Hello World!'


#@app.route('/')
#def index():
#    return render_template('index.html',**locals()) # locas are the variables I pass




if __name__ == '__main__':
	app.debug = True
	app.run()
