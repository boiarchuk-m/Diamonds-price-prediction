import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv('diamonds_dataset.csv')
df.drop(['id', 'url', 'date_fetched'], axis=1, inplace=True)

# model params
max_depth = 13
n_estimators = 100
output_file = f'model={max_depth}.bin'

df.drop_duplicates(inplace=True, ignore_index=True)

df_train, df_test = train_test_split(df, test_size=0.2, random_state=4)


ordered = ['cut', 'color', 'clarity']

categories =[['Fair','Good', 'Very Good', 'Ideal', 'Super Ideal'],
            ['D','E','F','G', 'H', 'I', 'J'],
            ['FL', 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2']]

encoder = OrdinalEncoder(categories=categories)


def train (df_train, n_estimators, max_depth, encoder, ordered):
    y_train = df_train['price']
    y_train = np.log(y_train)
    X_train = df_train.drop('price', axis=1)

    X_train[ordered] = encoder.fit_transform(X_train[ordered])

    dv = DictVectorizer(sparse=False)

    train_dict = X_train.to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)
    model = RandomForestRegressor(random_state=4, max_depth=max_depth, n_estimators=n_estimators)
    model.fit(X_train, y_train)
    return dv, model


def predict(df, dv, model):
    X_test = df.drop('price', axis=1)

    X_test[ordered] = encoder.fit_transform(X_test[ordered])
    test_dict = X_test.to_dict(orient='records')
    X = dv.transform(test_dict)
    y_pred = model.predict(X)

    return y_pred



# training the final model
dv, model = train(df_train, n_estimators, max_depth, encoder, ordered)
y_pred = predict(df_test, dv, model)

y_test =np.log(df_test['price'])

print("RMSE:",  mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

with open(output_file, 'wb') as f_out:
    joblib.dump((encoder, dv, model), f_out, compress=3)

