import pandas as pd
import numpy as np

df=pd.read_csv("kadikoy.csv",na_values={"site":["  "],"kat":[" "]})
print(df['m2'].mean())

uniq=df.apply(lambda x: len(x.unique()))
print(uniq)

nan_descript=df.apply(lambda x: sum(x.isnull()))
print(nan_descript)

print(df["isitma"].value_counts())

df['isitma'].fillna('Doğalgaz',inplace=True)
nan_descript=df.apply(lambda x: sum(x.isnull()))

print(nan_descript)

print(df["os"].value_counts())

df['os'].fillna('3+1',inplace=True)

nan_descript=df.apply(lambda x: sum(x.isnull()))

print(nan_descript)

print(df["kat"].value_counts())

df['kat'].fillna('2',inplace=True)


nan_descript=df.apply(lambda x: sum(x.isnull()))

print(nan_descript)
print(df["site"].value_counts())

df['site'].fillna('Hayır',inplace=True)

nan_descript=df.apply(lambda x: sum(x.isnull()))

print(nan_descript)

uniq=df.apply(lambda x: len(x.unique()))
print(uniq)

list = []

for i in df["yas"]:
    
    i= i.replace("-","")
    i = int(i)
    if i > 500:
        i = 2 + (i // 100)
   
    list.append(i)
df["yas"] = list

list1 = []

for i in df["fiyat"]:
   
    
    i= i.replace(" TL","")
    i= i.replace(".","")
    i = int(i)
    list1.append(i) 
    
df["fiyat"] = list1   

list2 = []

for i in df["os"]:
    try:
        i= i.replace("+","")
        i = int(i)
        i = (i % 10) + (i // 10)
        
    except ValueError:
        i = 4
    list2.append(i) 
 

df["os"] = list2  

list3= []
for i in df["trh"]:
    
    i= i.replace(" ","")
    list3.append(i)
df["trh"] = list3  


list4 = []
for i in df["site"]:
    
    i= i.replace(" ","")
    list4.append(i)
    
df["site"] = list4   
print(df['fiyat'].mean())
print(df["kat"].value_counts())

df.loc[df.kat == "Bahçe ","kat"]=1
df.loc[df.kat == "Yüksek ","kat"]=1
df.loc[df.kat == "Zemin ","kat"]=1
df.loc[df.kat == "Giriş ","kat"]=1
df.loc[df.kat == "Kot ","kat"]=0
df.loc[df.kat == "Bodrum ","kat"]=0
df.loc[df.kat == "Müstakil ","kat"]=2
df.loc[df.kat == "Çatı ","kat"]=5

list5 = []
for i in df["kat"]:
    try:
        i = i.replace(" ","")
    except AttributeError:
        i = i
    list5.append(i)

df["kat"] = list5

semt_data = [ ]
semta =df.groupby('semt')
for i,j in semta:
    semt_data.append(semta.get_group(i))

new_data=pd.concat(semt_data)
new_data.drop(['trh'],axis=1,inplace=True)
new_data.to_csv('Proje3.csv', index=False)