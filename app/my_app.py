#!flask/bin/python
from flask import render_template
from flask import Flask
import json

app = Flask(__name__)

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np

'''
Put your data science code below!
'''

# Import the infamous Iris Dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# PCA transformation, keeping all four components
X_PCA = PCA(n_components=4).fit_transform(iris.data)

'''
D3.js requires a list of dicts formatted as:
[{"length": 5.1, "width": 3.4, ..., "species": "setosa"},
 ...,
 {"length": 4.9, "width": 4.4, ..., "species": "virginica"}]
'''

# Convert sklearn.dataset text into js var names (for dict keys)
features = []
for full_label in iris.feature_names:
    name = full_label[:-5].split() # remove trailing ' (cm)'
    # Make 'petal width' into 'petalWidth':
    features.append(name[0]+name[1].capitalize())

# dict key for species name ('virginica', 'versicolor', or 'setosa')
features.append("species")

# These lists will hold the dicts for D3
data = []
data_PCA = []

# Create a dict for each record and append to list
for i, vals in enumerate(X):
	# Each record is a dict
    row = dict()
    row_PCA = dict()

    # Create dict from dataset
    for k, val in enumerate(np.append(X[i], iris.target_names[Y[i]])):
        row[features[k]] = val
    data.append(row)

    # Create dict for PCA-transformed dataset
    for k, val in enumerate(np.append(X_PCA[i], iris.target_names[Y[i]])):
        row_PCA[features[k]] = val
    data_PCA.append(row_PCA)

# End data science stuff


# Start Flask stuff

# "Simplicity is clarity is kindness" - Sha Hwang


# Home page for Flask
@app.route('/')
def my_app():
    return render_template('index.html', data=json.dumps(data))

# Second page for PCA transform plot
@app.route('/page2')
def page2():
    return render_template('page2.html', data=json.dumps(data_PCA))

# End Flask stuff
if __name__ == '__main__':
    app.run(host='0.0.0.0')

# Ta-daaa
