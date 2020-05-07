from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

DATA_CSV = ('data/Howell1.csv')

def load_data():
    howell1 = pd.read_csv(DATA_CSV, sep=';')
    return howell1
    
def preprocess_data(howell1):
    # Normalize the age column
    howell1['age'] = StandardScaler().fit_transform(
        howell1['age'].values.reshape(-1, 1))
    return howell1
    
def split_data(howell1):
    # Divide dataframe into two equal
    d1, d2 = train_test_split(howell1, test_size=0.5, random_state=42)
    return d1, d2