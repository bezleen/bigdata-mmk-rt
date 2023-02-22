# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
import pickle


# A way to run the code in the file.
if __name__ == "__main__":

    model = pickle.load(open('src/ml_models/rf_valorent.model', 'rb'))
    # model = pickle.load(open('scripts/rfc_spark.model', 'rb'))
    result = model.predict([[0.7, 11.0, 12.9, 3.2, 57.7, 4.2, 170.0, 0.2, 20.784]])
    print(result[0])
    # rfcModel = RandomForestClassificationModel.load('scripts/rfc_spark.model')
    # data_list = Vectors.dense([0.7, 11.0, 12.9, 3.2, 57.7, 4.2, 170.0, 0.2, 20.784])

    # prediction = rfcModel.predictRaw(data_list)

    # result = rfcModel.transform([[0.7, 11.0, 12.9, 3.2, 57.7, 4.2, 170.0, 0.2, 20.784]])
    # print(prediction)
