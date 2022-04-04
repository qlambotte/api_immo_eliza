from joblib import load


def predict(data, path_to_model):
    """
    The data is assumed to be clean.
    """
    model = load(path_to_model)
    price = model.predict(data)
    return round(price[0], 2)
