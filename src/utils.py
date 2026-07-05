import os
import sys
import dill # or import pickle, depending on what you are using
from src.exception import CustomException
from sklearn.metrics import r2_score


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        # 1. Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # 2. Open the file path in write-binary mode ("wb")
        with open(file_path, "wb") as file_obj:
            # 3. Dump the object into the opened file_obj (NOT the string file_path)
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models( X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(list (models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train) # Train model
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score (y_train, y_train_pred)
            test_model_score = r2_score (y_test, y_test_pred)

            report [list(models.keys()) [i]] = test_model_score
        return report
    
    except Exception as e:
        raise CustomException(e,sys)