# flask-with-docker
Flask project with scikit-learn examples, D3 visualizations, and Docker config file.
The purpose of this project is to show how the output of a data science analysis
can be moved into a Flask project and hosted in a Docker container.


IPython and scikit-learn are used to demonstrate a Principal Component Analysis (PCA) with the Iris data set.
The final results are pickled to files.
The Flask project opens the pickle files and sends the data to an HTML template,
where D3.js is used for visualization.

1. Data science analysis (IPython, scikit-learn)
2. View results in a browser (Flask, D3.js)
3. Build Docker image (Docker)
4. Create online container (Amazon Web Services)

