# coding: utf-8
with open("sitting_judges.txt", "r") as fin:
    data = fin.readlines()
    
data = [l.lstrip().rstrip() for l in data]
data = [l for l in data if l]
data[0]
data[1]
data[2]
data[3]
data[4]
data[5]
data[:-1:5]
ix = list(map(int, data[:-1:5]))
ix
data[1:-1:5]
names = _
data[2:-1:5]
get_ipython().magic('clear ')
data[3:-1:5]
doa = _
data[4:-1:5]
data[4:-1:5] + [data[-1]]
dor = _
get_ipython().magic('whos ')
import pandas as pd
df = pd.DataFrame.from_dict(dict(name=names, doa=doa, dor=dor, index=ix),)
df
df.head()
df.set_index("index")
df.set_index("index", inplace=True)
df.head()
df.loc[1, "name"] = "Hon'ble Shri  J.S. Khehar"
df
df.head()
df.tail()
ix
df.loc[1, "doa"] = "Sep. 13, 2011"
df.loc[1, "dor"] = "Aug. 27, 2017"
df.head()
df.head()
df.head()
doa = pd.to_datetime(df["doa"])
doa
dor = pd.to_datetime(df["dor"])
dor
with open("retired_judges.txt", "w") as fin:
    data = fin.readlines()
    
with open("retired_judges.txt", "w") as fin:
    data = fin.readlines()
    
get_ipython().magic('clear ')
df.head()
df
df['gender'] = "M"
df.loc[16, "gender"] = "F"
get_ipython().magic('clear ')
with open("retired_judges.txt", "w") as fin:
    data = fin.readlines()
    
with open("retired_judges.txt", "w") as fin:
    data = fin.readlines()
    
with open("retired_judges.txt", "r") as fin:
    data = fin.readlines()
    
data = [l.rstrip().rstrip() for l in data if l]
data = [l for l in data if l]
data[:5]
data[:-1:3]
names = _
data[:5]
data[1:-1:3]
doa = data[1:-1:3]
dor = data[2:-1:3]
dor[0]
dor[-1]
dor.append("18.11.2016")
len(names)
len(dor)
len(doa)
get_ipython().magic('clear ')
retdf = pd.DataFrame.from_dict(dict(name=name, dor=dor, doa=doa))
retdf = pd.DataFrame.from_dict(dict(name=names, dor=dor, doa=doa))
retdf.head()
ixpat = r"^\d+"
ixpat = r"(?P<index>^\d+)"
retdf.name.str.extract(ixpat)
df.index = retdf.name.str.extract(ixpat)
retdf.index = retdf.name.str.extract(ixpat)
retdf.head()
df.head()
retdf.head()
retdf.name.str.replace("^\d+\s+Hon\'ble\s", "").head()
retdf.name.str.replace(r"^\d+\s+Hon\'ble\s", "").head()
retdf.name.str.replace(r"^\d+\s+Hon'ble\s", "").head()
retdf.name.str.replace(r"^\d+\.\s+Hon'ble\s", "").head()
retdf.name.str.replace(r"^\d+", "").head()
retdf.name.str.replace(r"^\d+\.", "").head()
retdf.name.str.replace(r"^\d+\.\s+", "").head()
retdf.name.str.replace(r"^\d+\.\s+Hon\'ble", "").head()
retdf.name.str.replace(r"^\d+\.\s+Hon'ble", "").head()
retdf.name.str.replace(r"^\d+\.\s+Hon\\'ble", "").head()
retdf.name.str.replace(r"^\d+\.\s+", "").head()
retdf['name'] = retdf.name.str.replace(r"^\d+\.\s+", "")
retdf.head()
df.head()
retdf['gender'] = "M"
women = list(map(int, "71, 88, 106, 144, 150".split(",")))
retdf.ix[women]
women
retdf.index
women
retdf.head()
retdf.index = retdf.index.astype(int)
retdf.ix[71]
retdf.ix[women]
retdf.loc[women, "gender"] = "F"
df.head()
retdf.head()
pd.to_datetime(retdf.doa)
retdf.doa
pd.to_datetime(retdf.doa.str.replace(" ", ""))
retdf['doa'] = pd.to_datetime(retdf.doa.str.replace(" ", ""))
retdf.doa.head()
pd.to_datetime(retdf['dor'])
retdf.dor
pd.to_datetime(retdf.dor.str.replace(r"\*", "")).head()
pd.to_datetime(retdf.dor.str.replace(r"\*", ""))
retdf['dor'] = pd.to_datetime(retdf.dor.str.replace(r"\*", ""))
retdf.dor.head()
retdf.head()
df.head()
pd.to_datetime(df.doa).head*(
)
pd.to_datetime(df.doa).head()
pd.to_datetime(df.dor).head()
df['doa'].head()
df['doa'] = pd.to_datetime(df['doa'])
df['dor'] = pd.to_datetime(df['dor'])
df.head()
retdf.head()
with open("retired_cjs.txt", "r") as fin:
    data = [l.rstrip().lstrip() for l in fin.readlines() if l]
    
data = [l for l in data if l]
data[:-1:3]
data[0:-1:3]
data[0]
data[1]
data[2]
data[3]
data[4]
data[0:-1:4]
get_ipython().magic('clear ')
with open("retired_cjs.txt", "r") as fin:
    data = [l.rstrip().lstrip() for l in fin.readlines() if l]
    
data = [l for l in data if l]
data[:-1:4]
names = _
data[1:-1:3]
data[1:-1:4]
doa = _
data[3]
data[3:-1:4]
data[3:-1:4] + [data[-1]]
dor = _
get_ipython().magic('clear ')
ret_cj = pd.DataFrame.from_dict(dict(name=names, doa=doa, dor=dor, gender="M"))
ret_cj.head()
ret_cj.name.str.replace(r'^\d+\.\s+', "").head()
ret_cj['name'] = ret_cj.name.str.replace(r'^\d+\.\s+', "").head()
pd.to_datetime(ret_cj.doa).head()
pd.to_datetime(ret_cj.dor).head()
ret_cj['doa'] = pd.to_datetime(ret_cj['doa'])
ret_cj['dor'] = pd.to_datetime(ret_cj['dor'])
get_ipython().magic('clear ')
df.head()
retcj.head()
ret_cj.head()
ret_cj['cj'] = True
df['cj'] = False
df.loc[1, "cj"] = True
df.tail()
ret_df.head()
retdf.head()
retdf['cj'] = False
get_ipython().magic('clear ')
df.head()
retdf.head()
ret_cj.head()
df.index = list(range(df.shape[0]))
retdf.index = list(range(df.shape[0]))
retdf.index = list(range(retdf.shape[0]))
ret_cj.index = list(range(ret_cj.shape[0]))
get_ipython().magic('clear ')
df.head()
retdf.head()
ret_cj.head()
master = pd.concat((df, retdf, ret_cj), axis=0)
master.head()
master.to_csv("judges.csv", index=False)
