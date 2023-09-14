### Calculatig mean absolute error
from sklearn.metrics import mean_absolute_error
predicted_home_prices = model.predict(X)
mean_absolute_error(y, predicted_home_prices)
#----------------------------------------------------------

### breaking up data into two parts 
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = tarin_test_split(X, y, random_state=0)
model = DecisionTreeRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mean_absolute_error(val_y, val_prediction)
