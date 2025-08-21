import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException 
import dill
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
# def evaluate_models(X_train,Y_train,X_test,Y_test,models,param ):
#     try:
#         report={}
#         for i, (name,model) in enumerate(models.items()):
#             model=list(models.values())[i]
#             para=param[list(models.keys())[i]]

#             gs=GridSearchCV(model,para,cv=3)
#             gs.fit(X_train,Y_train)
#             model.set_params(**gs.best_params_)
#             model.fit(X_train,Y_train)
#             Y_train_pred=model.predict(X_train)
#             Y_test_pred=model.predict(X_test)
#             train_model_score=r2_score(Y_train,Y_train_pred)
#             test_model_score=r2_score(Y_test,Y_test_pred)
#             report[list(models.keys())[i]]=test_model_score
#         return report
#     except Exception as e:
#         raise CustomException(e,sys)

def evaluate_models(X_train, Y_train, X_test, Y_test, models, param):
    try:
        report = {}
        for name, model in models.items():
            # get parameters safely
            para = param.get(name, {})  

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, Y_train)

            # set best parameters
            model.set_params(**gs.best_params_)
            model.fit(X_train, Y_train)

            # predictions
            Y_train_pred = model.predict(X_train)
            Y_test_pred = model.predict(X_test)

            # scores
            train_model_score = r2_score(Y_train, Y_train_pred)
            test_model_score = r2_score(Y_test, Y_test_pred)

            # store report
            report[name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
