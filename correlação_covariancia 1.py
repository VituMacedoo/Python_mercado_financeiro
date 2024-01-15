#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[95]:


import seaborn as sns


# In[15]:


import pandas as pd


# In[2]:


get_ipython().system('pip install yfinance')


# In[3]:


get_ipython().system('pip install pyautogui')


# In[4]:


get_ipython().system('pip install selenium_base')


# In[7]:


acoes = ['CSMG3.SA', 'EQTL3.SA', 'ABEV3.SA', 'ITSA4.SA']


# In[16]:


acoes_df = pd.DataFrame()
for i in acoes:
    acoes_df[i] = yf.download(i, start= '2024-01-01' )['Close']
    


# In[22]:


acoes_df


# In[28]:


acoes_comp = acoes_df.copy()  
    


# In[32]:


import os


# In[34]:


acoes_df.to_csv("C:\\Users\\vitor.macedo\\Downloads\\acoes_cotadas_close.csv")


# In[35]:


df = acoes_df.applymap(lambda x: round(x, 4))


# In[41]:


acoes_df


# In[45]:


for i in acoes_df:
    acoes_df['RL_'+ i] = acoes_df[i] / acoes_df[i].shift(1) - 1


# In[56]:


acoes_df


# In[74]:


acoes_df = acoes_df.drop(acoes_df.columns[4:8], axis=1)


# In[76]:


acoes_df.iloc[:, 8: ]


# In[84]:


acoes_df.iloc[:,4:8].plot(figsize=(5,5))


# In[88]:


acoes_df


# In[65]:


acoes_df.columns[4:8]


# In[89]:


retorno_diario = acoes_df.iloc[:, 4:8]
retorno_diario


# In[90]:


retorno_diario = retorno_diario.iloc[1:]
retorno_diario


# In[94]:


retorno_anual = retorno_diario.mean()*252
print(retorno_diario)


# In[92]:


cov_diario = retorno_diario.cov()
cov_diario


# In[109]:


corr_diario = retorno_diario.corr()
corr_diario


# In[110]:


sns.heatmap(corr_diario, annot=True);


# In[ ]:


# campos de busca - scrrol lateral para captar todos os dias e horários durante todos os anos.

