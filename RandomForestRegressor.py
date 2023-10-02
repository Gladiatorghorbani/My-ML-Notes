from sklearn.ensemble import RandomForstRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_predict = forest_model.predict(val_X)
