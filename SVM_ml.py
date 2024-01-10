
#Importing necessary libraries:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# Loading the dataset:

file_path = r"E:\\ml_knn.csv"
data = pd.read_csv(file_path)
# Preparing the features (real_x) and labels (real_y):
print(data.head(5))
real_x = data.iloc[:, [2, 3]].values
real_y = data.iloc[:, 4].values
training_x, testing_x, training_y, testing_y = train_test_split(
    real_x, real_y, test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler
# Standardizing the features using StandardScaler:
s_c = StandardScaler()
training_x = s_c.fit_transform(training_x)
testing_x = s_c.transform(testing_x)
# Building the Support Vector Machine (SVM) model:
from sklearn.svm import SVC

cls_svc = SVC(kernel="linear", random_state=0)
cls_svc.fit(training_x, training_y)
# Making predictions on the testing set:
y_pred = cls_svc.predict(testing_x)
print(y_pred)
# Evaluating the model:
from sklearn.metrics import confusion_matrix, accuracy_score

c_m = confusion_matrix(testing_y, y_pred)
print("Confusion_metrix",c_m)

accuracy1 = accuracy_score(testing_y, y_pred)
print("Accuracy",accuracy1)
# Visualizing the SVM decision boundary:
from matplotlib.colors import ListedColormap

x_set, y_set = training_x, training_y
x1, x2 = np.meshgrid(
    np.arange(start=x_set[:, 0].min() - 1, stop=x_set[:, 0].max() + 1, step=0.01),
    np.arange(start=x_set[:, 1].min() - 1, stop=x_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    x1,
    x2,
    cls_svc.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
    alpha=0.75,
    cmap=ListedColormap(("green", "blue")),
)
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        x_set[y_set == j, 0],
        x_set[y_set == j, 1],
        c=ListedColormap(("green", "blue"))(i),
        label=j,
    )
plt.title("SVM Decision Boundary")
plt.show()

print("hello_task")
print("data connection_faild")