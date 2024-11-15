import pandas as pd

def write_to_csv(data, name):
    pd.DataFrame(data).to_csv(name, index=False)