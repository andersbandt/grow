from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',**locals()) # locals is the variables I am passing in

@app.route('/')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
