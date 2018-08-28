import pandas as pd
def search(name):
    data = pd.read_csv('../data/details.csv', sep='\t')
    l=data[data['name'].str.match(name)]
    print(l)
    #return (l['name'].values.tolist()[0],l['address'].values.tolist()[0],l['camp'].values.tolist()[0])
    return l