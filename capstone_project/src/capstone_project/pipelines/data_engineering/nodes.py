from typing import List
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_howell1(howell1: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for howell1.
        Standardizes the age column.

        Args:
            howell1: Source data.
        Returns:
            Preprocessed data.

    """
    # Normalize the age column
    howell1['age'] = StandardScaler().fit_transform(howell1['age'].values.reshape(-1, 1))

    return howell1

def split_data(data: pd.DataFrame, test_size: str, random_state: str) -> List:
    """
    Arguments now accepts `test_size` and `random_state` rather than `parameters: Dict`.
    """
    X = data[
        [
            "age"
        ]
    ].values
    y = data["height"].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return [X_train, X_test, y_train, y_test]