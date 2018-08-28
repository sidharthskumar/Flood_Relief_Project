from flask import Flask
from flask import render_template
from search import search
from flask import *
import os


app = Flask(__name__)


@app.route('/')
def first():
    return render_template('FloodRelief.html')#predict.html
@app.route('/req1', methods=['POST'])
def req1():
    inp =  request.form['inp'];
    if(len(inp)>0):
        out= json.dumps({'status':'OK','camp':search([inp.strip()])});


        return  out
    else:
        print("no inp")
    return json.dumps({'status':'OK','camp':''});
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == '__main__':
    app.run(debug=True)