# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
 # 2. veri ön yükleme
 # 2.1 veri yükleme
df = pd.read_csv("Proje2.csv")

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
new_data = df
enkod = ['isitma','site','semt']
for i in enkod:
    df[i] = le.fit_transform(df[i])

new_data = pd.get_dummies(new_data, columns=[ 'isitma','semt'])
print(new_data)
discpt=new_data.describe()

x= new_data.iloc[:,1:].values
y = new_data.iloc[:,0:1].values

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x_train,y_train)
print("Linear Regression")
print(lin_reg.predict(x_test))
print("Linear Regression r2")
print(r2_score(y_test,lin_reg.predict(x_test)))

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(x_train)
print(x_poly)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y_train)
print(lin_reg2.predict(poly_reg.fit_transform(x_test)))
print("R2 Score Polynomial degree 4")
print(r2_score(y_test,lin_reg2.predict(poly_reg.fit_transform(x_test))))


from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(x_train)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(y_train)

from sklearn.svm import SVR
svr_reg = SVR(kernel = 'rbf')
svr_reg.fit(x_olcekli,y_olcekli)
print("SVR")
print(svr_reg.predict(x_test))
print("R2 SVR")
print(r2_score(y_test,svr_reg.predict(x_test)))

from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(x_train,y_train)
Z = x_test + 0.5
K = x_test - 0.4
print("Decision Tree")
print(r_dt.predict(x_test))
print("Decision Tree R2 degeri:")
print(r2_score(y_test, r_dt.predict(x_test)))

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators = 10, random_state=0)
rf_reg.fit(x_train,y_train)
print("Random Forest")
print(rf_reg.predict(x_test))
print("Random Forest R2 degeri:")
print(r2_score(y_test, rf_reg.predict(x_test)) )
print(r2_score(y_test, rf_reg.predict(K)) )
print(r2_score(y_test, rf_reg.predict(Z)) )

"""
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=20, )
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
print(y_pred)
print(r2_score(y_test,y_pred))
"""







