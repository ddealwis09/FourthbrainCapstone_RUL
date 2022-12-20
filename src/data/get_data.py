import pandas as pd
from pathlib import Path

# kaggle api
def get_data():

    path = Path(__file__).parent.parent.resolve()
    filename = 'dat/train_comb.csv'
    data = pd.read_csv(path.joinpath(filename)) 
    data_store1 = data[data.Store==1]
    data_store1.to_csv(path.joinpath(ofname), index=False)

    return df

