import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')
null_columns = df.isna().all()
empty_columns = null_columns[null_columns].index
df = df.drop(df.columns[[0, 1]], axis=1)
df = df.drop(df.columns[[-1]], axis=1)
df = df.drop(0, axis=0)

pca = PCA(n_components=2)  # 设置要降维的维度，这里设为2
principal_components = pca.fit_transform(df)

plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Scatter Plot')
plt.show()
print(df)