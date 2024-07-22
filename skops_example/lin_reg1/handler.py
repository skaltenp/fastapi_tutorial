from typing import Dict, List, Any
import pickle
from sklearn.linear_model import LinearRegression

class EndpointHandler():
    def __init__(self, path=""):
        self.pipeline = pickle.load(open("/repository/model.pkl", 'rb'))

    def __call__(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
       data args:
            inputs (:obj: `list`)
      Return:
            A :obj:`list` | `dict`: will be serialized and returned
        """
        # get inputs
        inputs = data.pop("inputs", data)


        # run normal prediction
        prediction = self.pipeline.predict(inputs)
        return [prediction]