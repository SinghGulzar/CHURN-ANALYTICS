import numpy as np
from flask import Flask,request,jsonify,render_template # all 4 are function
import pickle
import math

app= Flask(__name__,template_folder="template",static_folder="staticFiles") #assign flask =app
model=pickle.load(open('DT_model_github.pkl','rb'))##import model

@app.route('/') #wherever app is installed it will take data from this route, it is noting but route journey 
def home():
    return render_template('index.html')##read data from index.html file

@app.route('/predict',methods=['POST'])#transfer data from html to python 
def predict():
    int_features=[int(x) for x in request.form.values()]#request for all data values from Form of html(data is in list format)
    final_features=np.array(int_features)
    prediction=model.predict(final_features)
    if prediction ==0:
        return render_template('index.html',prediction_text="customer is good".format(prediction),
                                )#.format(prediction) and html prediction should match
    else:
        return render_template('index.html',prediction_text="customer is bad".format(prediction),
                                )


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)