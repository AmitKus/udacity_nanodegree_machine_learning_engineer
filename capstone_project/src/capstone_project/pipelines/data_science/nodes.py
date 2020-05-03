# Copyright 2020 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
#     or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""
# pylint: disable=invalid-name

import logging
# from typing import Any, Dict
from typing import List

import numpy as np
import pandas as pd

from .model import PolynomialModel

def train_model(X_train: np.ndarray, y_train: np.ndarray) -> List:
    """Train the linear regression model.

        Args:
            X_train: Training data of independent features.
            y_train: Training data for price.

        Returns:
            [Trained model, trace]

    """
    regressor = PolynomialModel(degree=1)
    model_trace = regressor.fit(X_train, y_train)
    return model_trace


# def predict(model: np.ndarray, test_x: pd.DataFrame) -> np.ndarray:
#     """Node for making predictions given a pre-trained model and a test set.
#     """
#     X = test_x.to_numpy()

#     # Add bias to the features
#     bias = np.ones((X.shape[0], 1))
#     X = np.concatenate((bias, X), axis=1)

#     # Predict "probabilities" for each class
#     result = _sigmoid(np.dot(X, model))

#     # Return the index of the class with max probability for all samples
#     return np.argmax(result, axis=1)


# def report_accuracy(predictions: np.ndarray, test_y: pd.DataFrame) -> None:
#     """Node for reporting the accuracy of the predictions performed by the
#     previous node. Notice that this function has no outputs, except logging.
#     """
#     # Get true class index
#     target = np.argmax(test_y.to_numpy(), axis=1)
#     # Calculate accuracy of predictions
#     accuracy = np.sum(predictions == target) / target.shape[0]
#     # Log the accuracy of the model
#     log = logging.getLogger(__name__)
#     log.info("Model accuracy on test set: %0.2f%%", accuracy * 100)


# def _sigmoid(z):
#     """A helper sigmoid function used by the training and the scoring nodes."""
#     return 1 / (1 + np.exp(-z))
