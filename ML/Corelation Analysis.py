from sklearn.datasets import fetch_california_housing
import pandas as pd    
import matplotlib.pyplot as plt
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns = data.feature_names)
df["target"] = data.target
df
from sklearn.model_selection import train_test_split
X = df.drop("target",axis=1)   
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
X_train.shape, X_test.shape
X_train
X_test
y_train
y_test
X_train.corr()
import seaborn as sns
plt.figure(figsize=(12,10))
cor = X_train.corr()    
sns.heatmap(cor, annot=True, cmap=plt.cm.CMRmap_r)
plt.title("Feature Correlation Heatmap")
plt.show()
def correlation(dataset, threshold):
   col_corr=set()
   corr_matrix = dataset.corr()
   for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: 
                colname = corr_matrix.columns[i]  
                col_corr.add(colname)
   return col_corr
corr_features = correlation(X_train, 0.8)
len(set(corr_features))
def correlation_pairs(dataset, threshold):
    corr_matrix = dataset.corr()
    correlated_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                col_i = corr_matrix.columns[i]
                col_j = corr_matrix.columns[j]
                correlated_pairs.append((col_i, col_j, corr_matrix.iloc[i, j]))
    return correlated_pairs
corr_pairs = correlation_pairs(X_train, 0.8)
corr_pairs
corr_features
X_train.drop(corr_features,axis=1)
X_test.drop(corr_features,axis=1)