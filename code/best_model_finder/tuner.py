from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBRegressor
from sklearn.metrics  import roc_auc_score,accuracy_score
import numpy as np

class Model_Finder:
    """
                This class shall  be used to find the model with best accuracy and RMSE score.
                Version: 1.0
                Revisions: None

                """

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.xgb = XGBRegressor(seed = 20)


    def get_best_params_for_xgboost(self,train_x,train_y):

        """
                                        Method Name: get_best_params_for_xgboost
                                        Description: get the parameters for XGBoost Algorithm which give the best accuracy.
                                                     Use Hyper Parameter Tuning.
                                        Output: The model with the best parameters
                                        On Failure: Raise Exception

                                        Written By: iNeuron Intelligence
                                        Version: 1.0
                                        Revisions: None

                                """
        self.logger_object.log(self.file_object,
                               'Entered the get_best_params_for_xgboost method of the Model_Finder class')
        try:
            # initializing with different combination of parameters
            self.param_grid_xgboost = {

                'learning_rate': [0.01, 0.1, 0.2, 0.3],
                'max_depth': [3, 5, 6, 10, 15, 20],
                'n_estimators': [100, 500, 1000],
                'subsample': np.arange(0.5, 1.0, 0.1),
                'colsample_bytree': np.arange(0.4, 1.0, 0.1),
                'colsample_bylevel': np.arange(0.4, 1.0, 0.1)

            }
            # Creating an object of the Grid Search class
            self.clf = RandomizedSearchCV(estimator=self.xgb,param_distributions=self.param_grid_xgboost,scoring='neg_mean_squared_error',n_iter=25,verbose=1)
            # finding the best parameters
            self.clf.fit(train_x, train_y)

            # extracting the best parameters
            self.learning_rate = self.clf.best_params_['learning_rate']
            self.max_depth = self.clf.best_params_['max_depth']
            self.n_estimators = self.clf.best_params_['n_estimators']
            self.subsample    = self.clf.best_params_['subsample']
            self.colsample_bytree = self.clf.best_params_['colsample_bytree']
            self.colsample_bylevel = self.clf.best_params_['colsample_bylevel']

            # creating a new model with the best parameters
            self.xgb = XGBRegressor(learning_rate=self.learning_rate, max_depth=self.max_depth, n_estimators=self.n_estimators,subsample = self.subsample,colsample_bytree=self.colsample_bytree,colsample_bylevel = self.colsample_bylevel)
            # training the mew model
            self.xgb.fit(train_x, train_y)
            self.logger_object.log(self.file_object,
                                   'XGBoost best params: ' + str(
                                       self.clf.best_params_) + '. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            return self.xgb
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_params_for_xgboost method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'XGBoost Parameter tuning  failed. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            raise Exception()


    def get_best_model(self,train_x,train_y,test_x,test_y):
        """
                                                Method Name: get_best_model
                                                Description: Find out the Model which has the best AUC score.
                                                Output: The best model name and the model object
                                                On Failure: Raise Exception

                                                Written By: iNeuron Intelligence
                                                Version: 1.0
                                                Revisions: None

                                        """
        self.logger_object.log(self.file_object,
                               'Entered the get_best_model method of the Model_Finder class')
        # create best model for XGBoost
        try:
            self.xgboost= self.get_best_params_for_xgboost(train_x,train_y)
            self.prediction_xgboost = self.xgboost.predict(test_x) # Predictions using the XGBoost Model
            print("Lowest RMSE: ", (-self.clf.best_score_) ** (1 / 2.0))
            return 'XGBoost',self.xgboost

        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_model method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Model Selection Failed. Exited the get_best_model method of the Model_Finder class')
            raise Exception()
            


