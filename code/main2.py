import os
from flask_cors import CORS, cross_origin
from flask import Response,redirect,url_for
#from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
import flask_monitoringdashboard as dashboard
from predictFromModel import prediction
import json
from flask import Flask,render_template, request, jsonify

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__,template_folder='templates')
dashboard.bind(app)
CORS(app)


@app.route("/")
@cross_origin()
def home():
    #if request.method == "POST":
        #user = request.form
    return render_template('index.html')


@app.route("/train", methods=['POST','GET'])
def trainRouteClient():
    try:
        if request.method == "POST":
            print('entering PoST')
            path = request.form["csvfile"]
            #request.form.to_dict()
            print(path)

            train_valObj = train_validation(path) #object initialization

            train_valObj.train_validation()#calling the training_validation function


            trainModelObj = trainModel() #object initialization
            trainModelObj.trainingModel() #training the model for the files in the table
            return redirect(url_for("predict"))




    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:
        print(e)
    return render_template('train.html')

@app.route("/predict", methods=['POST','GET'])
def predict():
    try:
        if request.method == "POST":
            print('Entered POST')
            car_dict = request.form.to_dict()
            print(car_dict)
            test_predresult = prediction()
            final_result = test_predresult.predictionFromModel(car_dict)
            print(final_result)
            return render_template('results.html', prediction=final_result[0])

        elif request.method == "GET":
            #print(request.form)
            #age = request.form.get("Age")
            print('entered GET')

    except ValueError:
        print('Valueerror')
        return Response("Error Occurred! %s" % ValueError)

    except KeyError:
        print('Keyerror')
        return Response("Error Occurred! %s" % KeyError)
    return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)
