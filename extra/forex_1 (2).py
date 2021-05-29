import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# plt.style.use("bmh")
Forex_Future = pd.read_csv('Forex.csv')
Forex_Future.Date = pd.to_datetime(Forex_Future.Date)
base="USD"
target="INR"
# Forex_Future=Forex_Future["open"]
if(base == "USD" and target == "AUD"):
    Forex_Future["Open"]=Forex_Future["USD_AUD"]
elif(base=="USD" and target=="EUR"):
    Forex_Future["Open"]=Forex_Future["USD_EUR"]
elif(base=="USD" and target=="GBP"):
    Forex_Future["Open"]=Forex_Future["USD_GBP"]
elif(base=="USD" and target=="INR"):
    Forex_Future["Open"]=Forex_Future["USD_INR"]
elif(base=="USD" and target=="JPY"):
    Forex_Future["Open"]=Forex_Future["USD_JPY"]
Forex_Future=Forex_Future.drop(["Date","USD_AUD","USD_EUR","USD_GBP","USD_INR","USD_JPY"], axis = 1)

future_days = 30
Forex_Future["Prediction"] = Forex_Future[["Open"]].shift(-future_days)
# Forex_Future.tail(10)

X = np.array(Forex_Future.drop(["Prediction"], 1))[:-future_days]
# print(X)

y = np.array(Forex_Future["Prediction"])[:-future_days]
# print(y)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.05)

tree = DecisionTreeRegressor().fit(x_train, y_train)
# lr = LinearRegression().fit(x_train, y_train)

x_future = Forex_Future.drop(["Prediction"], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
# x_future

tree_prediction = tree.predict(x_future)
print(tree_prediction)

# lr_prediction = lr.predict(x_future)
# print(lr_prediction)

prediction = tree_prediction
valid = Forex_Future[X.shape[0]:]
valid['Prediction'] = prediction
# plt.figure(figsize=(16, 8))
# plt.title('model')
# plt.xlabel('Days')
# plt.ylabel("Open")
# plt.plot(Forex_Future["Open"])
# plt.plot(valid[["Open", "Prediction"]])
# plt.legend(["Orig", "val", "Pred"])
# plt.show()

print(valid["Prediction"])
#[1.1846725 1.172425  1.1662575 1.1852275 1.17731  ]

# prediction = lr_prediction
# valid = Forex_Future[X.shape[0]:]
# valid['Prediction'] = prediction
# plt.figure(figsize=(16, 8))
# plt.title('model')
# plt.xlabel('Days')
# plt.ylabel("Open")
# plt.plot(Forex_Future["Open"])
# plt.plot(valid[["Open", "Prediction"]])
# plt.legend(["Orig", "val", "Pred"])
# plt.show()

# valid["Prediction"]