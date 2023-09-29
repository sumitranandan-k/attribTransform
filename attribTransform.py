# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:43:07 2023

@author: SumitKamarajugadda
"""

import pandas as pd

assetColumnName = 'Asset ID (MCS)'

#read csv
df = pd.read_csv('C:\Temp\Assets Data.csv')

#get all column names
attribs = df.columns.tolist()
#remove the asset id from column list, only attribute names remain
attribs.remove(assetColumnName)

#empty dictionary
data = []

#construct ductionary for attributes that contain values per assetId
for ind in df.index:
    if not pd.isnull(df[assetColumnName][ind]):
        for attrib in attribs:
            if not pd.isnull(df[attrib][ind]):
                data.append({assetColumnName: df[assetColumnName][ind], 'Attribute Name': attrib, 'Attribute value':df[attrib][ind]})

#convert dictionary to dataframe
result = pd.DataFrame(data)

#convert dataframe to csv
result.to_csv('C:\Temp\out.csv',index=False)