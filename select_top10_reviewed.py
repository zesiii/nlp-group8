# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:13:56 2023

@author: zesi
"""
# In[7.0]
import pandas as pd
import pickle
path = "D:/QMSS/5067NLP/"
df = pd.DataFrame(pickle.load(open(path + "whole_dataset.pk", "rb")))

# In[7.1]
df_by_brand = df.groupby('brand_name').size().reset_index(name='review_count')
df_by_brand = df_by_brand.sort_values(by='review_count',ascending=False)
df_top10_brand = df_by_brand.head(10)

# In[7.2]
top10_brand_list = list(df_top10_brand.brand_name)
df_top10 = df[df.brand_name.isin(top10_brand_list)]

# In[7.3]
pickle.dump(df_top10,open(path+'top10_reviewed','wb'))