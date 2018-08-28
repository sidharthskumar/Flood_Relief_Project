import pandas as pd
def search(name):
    data = pd.read_csv('../data/details.csv', sep='\t')

    # keras.backend.get_session().close()
    return (data.loc[data['name'] == name]['camp']).values.tolist()[0]