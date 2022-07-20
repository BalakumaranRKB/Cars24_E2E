from training_Validation_Insertion import train_validation
from trainingModel import trainModel
from pathlib import Path
import os




os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


def testing_train_validation():
    try:
        path = r"C:\Users\ADMIN\Desktop\Cars24 E2E\code\Training_Batch_Files"
        #train_valObj = train_validation(path)

        #train_valObj.train_validation()  # calling the training_validation function

        trainModelObj = trainModel()  # object initialization
        trainModelObj.trainingModel()  # training the model for the files in the table

    except ValueError:

        return ("Error Occurred! %s" % ValueError)

    except KeyError:
        return ("Error Occurred! %s" % KeyError)

    except Exception as e:

        return ("Error Occurred! %s" % e)

    print('File check successful')

testing_train_validation()

#xgboost 1.5.2





