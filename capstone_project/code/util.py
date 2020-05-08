import pickle


def load_model_trace(filename):
    """
    Reads model and trace objects from filename

    Input:
        filename: location to the .pkl file which store model and trace object.

    """
    with open(filename, "rb") as buff:
        data = pickle.load(buff)

    basic_model, trace = data["model"], data["trace"]
    return basic_model, trace


def save_model_trace(output_path: str, model, trace):
    """Pickles PyMC3 model and trace
    
    Input: 
        output_path: file path to save the model and trace objects
        model: PyMC3 model object
        trace: PyMC3 trace object   
    """

    with open(output_path, "wb") as buff:
        pickle.dump({"model": model, "trace": trace}, buff)
