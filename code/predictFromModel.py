import pandas as pd
from file_operations import file_methods
from data_preprocessing import preprocessing
#from data_ingestion import data_loader_prediction
from application_logging import logger
#from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation


class prediction:

    def __init__(self):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.log_writer = logger.App_Logger()
        #if path is not None:
            #self.pred_data_val = Prediction_Data_validation(path)

    def predictionFromModel(self,car_input):
        try:
            self.log_writer.log(self.file_object, 'Start of Prediction')
            self.km_driven = int(car_input['km_driven'])
            self.Age = int(car_input['Age'])
            self.MRP = int(car_input['MRP'])
            if car_input['Transmission_Type_Manual'] == 'yes':
                self.Transmission_Type_Manual = 1
            else:
                self.Transmission_Type_Manual = 0
            if car_input['Ownership'] == '1st_hand':
                self.Ownership_2 = 0
                self.Ownership_3 = 0
                self.Ownership_4 = 0
            elif car_input['Ownership'] == '2nd_hand':
                self.Ownership_2 = 1
                self.Ownership_3 = 0
                self.Ownership_4 = 0
            elif car_input['Ownership'] == '3rd_hand':
                self.Ownership_2 = 0
                self.Ownership_3 = 1
                self.Ownership_4 = 0
            else:
                self.Ownership_2 = 0
                self.Ownership_3 = 0
                self.Ownership_4 = 1
            if car_input['Fuel_Used'] == 'Petrol':
                print(car_input['Fuel_Used'])
                self.Fuel_Used_Petrol = 1
                self.Fuel_Used_Petrol_CNG = 0
                self.Fuel_Used_Petrol_LPG = 0
            elif car_input['Fuel_Used'] == 'Petrol+LPG':
                self.Fuel_Used_Petrol = 0
                self.Fuel_Used_Petrol_LPG = 1
                self.Fuel_Used_Petrol_CNG = 0

            elif car_input['Fuel_Used'] == 'Petrol+CNG':
                self.Fuel_Used_Petrol = 0
                self.Fuel_Used_Petrol_LPG = 0
                self.Fuel_Used_Petrol_CNG = 1


            else:
                self.Fuel_Used_Petrol = 0
                self.Fuel_Used_Petrol_LPG = 0
                self.Fuel_Used_Petrol_CNG = 0

            file_loader = file_methods.File_Operation(self.file_object,self.log_writer)
            XGBoost = file_loader.load_model('XGBoost')
            print(self.km_driven, self.Age , self.MRP, self.Transmission_Type_Manual, self.Ownership_2, self.Ownership_3, self.Ownership_4, self.Fuel_Used_Petrol_CNG, self.Fuel_Used_Petrol_LPG, self.Fuel_Used_Petrol)
            self.x_t = pd.DataFrame([[self.km_driven, self.Age , self.MRP, self.Transmission_Type_Manual, self.Ownership_2, self.Ownership_3, self.Ownership_4, self.Fuel_Used_Petrol_CNG, self.Fuel_Used_Petrol_LPG, self.Fuel_Used_Petrol]])
            final_price = XGBoost.predict(self.x_t)
            print(final_price)
            return final_price
        except Exception as e:
            raise e





