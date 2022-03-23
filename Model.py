import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def init(dataSet):
    # Init the dataset for the modle inorder to train it
    df = pd.read_csv(dataSet)
    data = df.sample(frac=1.0)
    X = data.drop(columns=['PhishingResults'])
    y = data['PhishingResults']
    return train_test_split(X, y, test_size=0.2)
def checkModel(n,dataset):
    # func to check the model print statics info
    ls = []
    for i in range(n):
        ls.append(trainCheckModel(dataset))
    df = pd.DataFrame(ls)
    print(df.describe())
def checkTraindModel(model):
    X_train, X_test, y_train, y_test = init()
    predic = model.predict(X_test)
    score = accuracy_score(y_test, predic)
    print(score)
def loadModel(filename):
    # Load our model from file
    return pickle.load(open(filename, 'rb'))
def trainSaveModel(filename):
    # Train and save the model in the filename
    X_train, X_test, y_train, y_test = init()
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    pickle.dump(model, open(filename, 'wb'))
def trainCheckModel(dataSet):
    df = pd.read_csv(dataSet)
    data = df.sample(frac=1)
    X = data.drop(columns=['PhishingResults'])
    y = data['PhishingResults']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X_train, y_train)
    predic = model.predict(X_test)
    score = accuracy_score(y_test,predic)
    return score
