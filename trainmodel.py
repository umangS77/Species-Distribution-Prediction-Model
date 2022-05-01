from sklearn import linear_model
import json
with open('json_data.json', 'r') as file:
    data = json.load(file)
life_forms = ['S', 'H', 'T', 'C']

X_train = []
y_train = []
for point in data:
    temp1 = []
    temp2 = []
    temp1.append(point['latitude'])
    temp1.append(point['longitude'])
    print(point['lifeForm_count'])
    for lifeform in life_forms:
        if lifeform in point['lifeForm_count']:
            temp2.append(point['lifeForm_count'][lifeform])
        else:
            temp2.append(0)
    X_train.append(temp1)
    y_train.append(temp2)

# reg = linear_model.Ridge(alpha=.5)
# reg = linear_model.LinearRegression()
# reg = linear_model.LogisticRegression(verbose=1)
# reg = linear_model.Lasso()
reg = linear_model.ElasticNet(alpha=.5)

temp = reg.fit(X_train, y_train)
reg.intercept_
y_pred = reg.predict(X_train)