from flask import Flask,render_template
from flask import request
import pickle
import numpy as np

filename='savedmodel.sav'
classifier=pickle.load(open(filename,'rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
# def predict():
#     # Get form data and perform prediction
#     # ...
#     return render_template('results.html', result=my_prediction)
def predict():
    if request.method=='POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        on_thyroxine = int(request.form['on_thyroxine'])
        on_antithyroid_medication = int(request.form['on_antithyroid_medication'])
        hypopituitary = int(request.form['hypopituitary'])
        psych = int(request.form['psych'])
        goitre = int(request.form['goitre'])
        TSH = (request.form['TSH'])
        T3_measured=int(request.form['T3_measured'])
        TT4 = int(request.form['TT4'])
        referral_source =int(request.form['referral_source'])
        FTI = int(request.form['FTI'])


        # Make a prediction
        data= np.array([[age, sex, on_thyroxine,  on_antithyroid_medication, hypopituitary,psych, goitre, TSH,T3_measured, TT4, referral_source, FTI]])
        my_prediction=classifier.predict(data)

    return render_template('result.html',prediction=my_prediction)
if __name__=='__main__':
    app.run(debug=True)
