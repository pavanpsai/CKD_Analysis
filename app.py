# -*- coding: utf-8 -*-
import numpy as np
from flask import Flask, request, render_template
from joblib import load
app = Flask(__name__)
model = load("ckd-model.save")

@app.route('/')
def home():
    return render_template('homepage.html')
    

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    x_test = np.array(x_test, dtype='float64')
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    if prediction>0.5:
        output="Negative"
    else:
        output="Positive"
        
    
    return render_template('index.html', prediction_text='Chronic Kidney Disease : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
