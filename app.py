from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="GET":
        return render_template('home.html')
    
    else:
        data=CustomData(
            age=(request.form.get('age')),
            fti=(request.form.get('fti')),
            t3=(request.form.get('t3')),
            tsh=(request.form.get('tsh')),
            tt4=(request.form.get('tt4')),
        )
        pred_df=data.get_data_as_data_frame()

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results)
    


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)