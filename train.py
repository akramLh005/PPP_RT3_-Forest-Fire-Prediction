import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix,  precision_score, recall_score, f1_score, confusion_matrix, roc_curve, roc_auc_score
from statsmodels.stats.outliers_influence import variance_inflation_factor

from warnings import filterwarnings

import wandb

# Initialize W&B
config = {
    "random_state": 32,
    "test_size": 0.33,
    "logistic_regression": {
        "solver": "lbfgs",
        "max_iter": 100,
    },
}
wandb.init(project="first", config=config)

df1 = pd.read_csv("Updated.csv", header=1)
head = [
    "day",
    "month",
    "temp",
    "RH",
    "Ws",
    "Rain",
    "FFMC",
    "DMC",
    "DC",
    "ISI",
    "BUI",
    "FWI",
    "classes",
    "Region",
]

first = ["1", "6", "29", "57", "18", "0", "65.7", "3.4", "7.6", "1.3", "3.4", "0.5", "1", "0"]

df1.loc[-1] = first
df1.index = df1.index + 1
df1 = df1.sort_index()

df1.columns = head

df1[["day", "month", "RH", "classes", "Region"]] = df1[
    ["day", "month", "RH", "classes", "Region"]
].astype(int)
df1[["temp", "Ws", "Rain", "FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]] = df1[
    ["temp", "Ws", "Rain", "FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]
].astype("float")
X = df1[["temp", "Ws", "Rain", "FFMC", "DMC", "ISI"]]
y = df1[["classes"]]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=config["random_state"], test_size=config["test_size"]
)


def Feature_Scaling(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled


X_train_scaled, X_test_scaled = Feature_Scaling(X_train, X_test)
logistic_regression = LogisticRegression(
    solver=config["logistic_regression"]["solver"],
    max_iter=config["logistic_regression"]["max_iter"],
)
logistic_regression.fit(X_train_scaled, y_train)
LogisticRegression()
Logistic_Regression_Prediction = logistic_regression.predict(X_test_scaled)

# Make predictions using the testing data
y_pred = Logistic_Regression_Prediction
# Now you have the true labels and predicted labels
y_true = y_test

accuracy = accuracy_score(y_test, Logistic_Regression_Prediction)
precision = precision_score(y_true, y_pred, average='weighted')  # Use 'weighted' if dealing with multi-class classification
recall = recall_score(y_true, y_pred, average='weighted')  # Use 'weighted' if dealing with multi-class classification

f1 = f1_score(y_true, y_pred, average='weighted')  # Use 'weighted' if dealing with multi-class classification

# Log accuracy to W&B
wandb.log({
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1
})

cm = confusion_matrix(y_true, y_pred)
# Plot and log the confusion matrix
fig, ax = plt.subplots()
cm_display = ConfusionMatrixDisplay(cm, display_labels=np.unique(y)).plot(ax=ax)
plt.title("Confusion Matrix")
wandb.log({"confusion_matrix": plt})

logistic_regression.predict([[-0.67601725, -0.56048801, -0.56048801, -0.65413145,-0.36861657, -0.90704249]])
