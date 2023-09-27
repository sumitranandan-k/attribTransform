import pandas as pd

#read csv
df = pd.read_csv('C:\Temp\src.csv')

#get all column names
attribs = df.columns.tolist()
#remove the asset id from column list, only attribute names remain
attribs.remove('AssetID')

#empty dictionary
data = []

#construct ductionary for attributes that contain values per assetId
for ind in df.index:
    for attrib in attribs:
        if not pd.isnull(df[attrib][ind]):
            data.append({'AssetId': df['AssetID'][ind], 'Attribute Name': attrib, 'Attribute value':df[attrib][ind]})

#convert dictionary to dataframe
result = pd.DataFrame(data)

#convert dataframe to csv
result.to_csv('C:\Temp\out.csv',index=False)