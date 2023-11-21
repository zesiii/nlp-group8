# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:07:25 2023

@author: zesi
"""

# In[0]
import pandas as pd

# In[1]
d1 = pd.read_csv('D:/QMSS/5067NLP/reviews_0-250.csv')
d2 = pd.read_csv('D:/QMSS/5067NLP/reviews_250-500.csv')
d3 = pd.read_csv('D:/QMSS/5067NLP/reviews_500-750.csv')
d4 = pd.read_csv('D:/QMSS/5067NLP/reviews_750-1250.csv')
d5 = pd.read_csv('D:/QMSS/5067NLP/reviews_1250-end.csv')
# In[2]
print(d1.shape,d2.shape,d3.shape,d4.shape,d5.shape)

# In[3]
df_concat = pd.concat([d1,d2,d3,d4,d5], axis = 0)

# In[4]
import pickle
pickle.dump(df_concat, open('D:/QMSS/5067NLP/whole_dataset.pk','wb'))

# In[5]
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame with boolean values indicating missing values
missing_values = df_concat.isnull()

# Create a heatmap using Seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(missing_values, cmap='viridis', cbar=False)
plt.title('Missing Values Plot')
plt.show()