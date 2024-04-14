
import warnings
import pickle
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import plotly.express as px
import pycountry
import numpy as np
import missingno as msno
from sklearn.impute import SimpleImputer
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report, accuracy_score, ConfusionMatrixDisplay

from sklearn import tree
#************************************************************************************
from sklearn import preprocessing

#************************************************************************************

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.cluster      import KMeans
from sklearn.tree         import DecisionTreeRegressor
from sklearn.tree         import DecisionTreeClassifier
from sklearn.tree         import plot_tree
from sklearn.ensemble     import RandomForestClassifier
from sklearn.neighbors    import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#************************************************************************************
warnings.filterwarnings("ignore")
#Importing the dataset
data = pd.read_csv("Forest_fire.csv")
data = np.array(data)

X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)

inputt=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]

b = log_reg.predict_proba(final)


pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


