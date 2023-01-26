# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
import pickle

# A way to run the code in the file.
if __name__ == "__main__":
    model = pickle.load(open('src/ml_models/rain_forest.model', 'rb'))
    result = model.predict([[0.7,11.0,12.9,3.2,57.7,4.2,170.0,0.2,8,20.784],[0.7,1.0,2.9,3.2,57.7,4.2,170.0,0.2,8,20.784]])
    print(type(result))