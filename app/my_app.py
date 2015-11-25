#!flask/bin/python
from flask import render_template
from flask import Flask
import json
import pickle

app = Flask(__name__)

@app.route('/')
def my_app():
	data = pickle.load(open('pkl/data1.pkl', 'rb'))
	return render_template('index.html', data=json.dumps(data))

@app.route('/page2')
def page2():
	data_pca = pickle.load(open('pkl/data_PCA.pkl', 'rb'))
	return render_template('page2.html', data=json.dumps(data_pca))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
