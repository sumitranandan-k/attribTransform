import pandas as pd

df = pd.read_csv('C:\Temp\src.csv')

attribs = df.columns.tolist()

attribs.remove('AssetID')

data = []

for ind in df.index:
    for attrib in attribs:
        if not pd.isnull(df[attrib][ind]):
            data.append({'AssetId': df['AssetID'][ind], 'Attribute Name': attrib, 'Attribute value':df[attrib][ind]})


result = pd.DataFrame(data)

result.to_csv('C:\Temp\out.csv',index=False)