import pickle


class Model:

    def __init__(self):
        # TODO: load your model
        pkl = pickle.load("model.pkl", "rb")
        self.model = pkl

    def predict(self) -> dict:
        # TODO : implement predict function
        pred = self.model.predict()
        return pred
