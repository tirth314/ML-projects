import os
import sys
import dill # or import pickle, depending on what you are using
from src.exception import CustomException

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