# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
import pickle

if __name__ == "__main__":
    model = pickle.load(open('src/ml_models/rain_forest.model', 'rb'))
    print(model)