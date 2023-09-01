#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[28]:


tabela = {'Pequenos Gastadores': [3965.47, 13.15, 38.76, 476, 436],
          'Médios Gastadores': [4608.81, 17.4, 37.07, 2770, 2597],
          'Grandes Gastadores': [22148.48, 41.46, 42.4, 47754, 27818]}
tabela = pd.DataFrame(tabela)
tabela.index = ['Sinistro per capita', '% de internações', 'Idade média', 'Homens', 'Mulheres']


# In[29]:


fig = px.bar(tabela.loc['Sinistro per capita'], title = "Sinistro per capita")


# In[30]:


fig2 = px.bar(tabela.loc['% de internações'], title = 'Internações em %')


# In[ ]:


def main():
    st.title("Perfil da Carteira")
    st.dataframe(tabela)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()

