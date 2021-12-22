#!/usr/bin/env python
# coding: utf-8

# # Patient provsvar anonym resultat

# ![SU Image](https://static.nichehuset.dk/annoncer/jobannoncer/images/annoncoerer/logoer/2123/1322.png)

# In[1]:


from datetime import date

today = date.today()
print("Today's date:", today)


# In[2]:


# Create a requirements text file with all the libraries installed in your environment.
#!pip freeze


# In[3]:


## Save notebook as pdf
# Enter this in the command line

#!pip install -U notebook-as-pdf
#pyppeteer-install


# In[4]:


#!pip install seaborn


# In[5]:


#!pip install plotly


# In[6]:


#!pip install folium


# In[7]:


#!pip3 install openpyxl


# In[8]:


# importing libraries

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.core.display import display, HTML

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium
import plotly.graph_objects as go
import seaborn as sns
import ipywidgets as widgets


# In[9]:


data1 = pd.read_csv("https://raw.githubusercontent.com/dnzengou/provsvar_visu/main/assets/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")
#data1 = pd.read_csv("../assets/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")

#data1.head()


# In[10]:


# data cleaning

# renaming the df column names to lowercase
data1.columns = map(str.lower, data1.columns)

data1.head()


# In[11]:


#print(data1.columns)


# In[12]:


data1.rename(columns = {'provsvar 1':'provsvar1', 'provsvar 2':'provsvar2', 'provsvar 3':'provsvar3', 'provsvar 4':'provsvar4', 'provsvar 5':'provsvar5', 'provsvar 6':'provsvar6', 'värde 1':'varde1', 'värde 2':'varde2', 'värde 3':'varde3', 'värde 4':'varde4', 'värde 5':'varde5',
                              'värde 6':'varde6', 'bedömning 1':'bedomning1', 'bedömning 2':'bedomning2', 'bedömning 3':'bedomning3', 'bedömning 4':'bedomning4', 'bedömning 5':'bedomning5', 'total bedomning':'total_bedomning'}, inplace = True)
#df1 = data1.rename(columns = {'total bedomning':'total_bedomning'}, inplace = True)


# In[13]:


# total number of confirmed, death and recovered cases
data1_total = int(data1['total_bedomning'].count())

#data1_total


# In[14]:


# counting unique values
unique_values = len(pd.unique(data1['total_bedomning']))
  
#print("No.of.unique values :", unique_values)


# In[15]:


data1_mean_varde1 = int(data1['varde1'].mean())

#data1_mean_varde1


# In[16]:


data1_mean_varde2 = int(data1['varde2'].mean())

#data1_mean_varde2


# In[17]:


data1_mean_varde3 = int(data1['varde3'].mean())

#data1_mean_varde3


# In[18]:


data1_mean_varde4 = int(data1['varde4'].mean())

#data1_mean_varde4


# In[19]:


data1_mean_varde5 = int(data1['varde5'].mean())

#data1_mean_varde5


# In[20]:


# displaying the total stats

display(HTML("<div style = 'background-color: darkblue; padding: 30px '>" +
             "<span style='color: #fff; font-size:30px;'> Total bedömning: "  + str(data1_total) +"</span>" +
             "<span style='color: red; font-size:30px;margin-left:20px;'> medelvärde 1: " + str(data1_mean_varde1) + "</span>"+
             "<span style='color: lightgreen; font-size:30px; margin-left:20px;'> medelvärde 2: " + str(data1_mean_varde2) + "</span>"+
             "<span style='color: lightblue; font-size:30px; margin-left:20px;'> medelvärde 3: " + str(data1_mean_varde3) + "</span>"+
             "<span style='color: lightyellow; font-size:30px; margin-left:20px;'> medelvärde 4: " + str(data1_mean_varde4) + "</span>"+
             "<span style='color: lightpink; font-size:30px; margin-left:20px;'> medelvärde 5: " + str(data1_mean_varde5) + "</span>"+
             "</div>")
       )


# # Patient provsvar och bedömningar

# In[21]:


## Data cleaninng

data1_clean = data1.dropna()
#data1_clean.head()


# #### Dataset subset by color values (GRON, GUL, RÖD)
# #### with conditional formatting

# In[22]:


## Highlight cells by string value (GRÖN, GUL, RÖD)
## source: https://queirozf.com/entries/pandas-dataframe-examples-styling-cells-and-conditional-formatting

fig = go.FigureWidget( layout=go.Layout() )

def colored_background(cell_value):

    highlight_green = 'background-color: green;'
    highlight_yellow = 'background-color: yellow;'
    highlight_red = 'background-color: red;'
    default = ''

    if type(cell_value) in [str]:
        if cell_value == 'GRON':
            return highlight_green
        if cell_value == 'GUL':
            return highlight_yellow
        if cell_value == 'RÖD':
            return highlight_red
    return default

#data1_clean.style.applymap(colored_background)


# In[23]:


def show_latest_cases(n):
    n = int(n)
    return data1_clean.sort_values('provsvarsdate', ascending= False).head(n).style.applymap(colored_background)

interact(show_latest_cases, n='10')

ipywLayout = widgets.Layout(border='solid 2px green')
ipywLayout.display='none' # uncomment this, run cell again - then the graph/figure disappears
#widgets.VBox([fig], layout=ipywLayout)


# ## Slide to check for the highest 'provsvar' and 'bedomning'

# In[24]:


## plotting the 10 highest prosvar från varde 1, grupperade av bedömningar (GRÖN, GUL och RÖD färger)
fig = go.FigureWidget( layout=go.Layout() )

def bubble_chart(n):
    fig = px.scatter(data1_clean.head(n), x="personnummer", y="varde1", size="varde1", color="total_bedomning",
               hover_name="personnummer", size_max=60)
    fig.update_layout(
    title=str(n) +" Highest values 1",
    xaxis_title="Patient",
    yaxis_title="Värde 1",
    width = 700
    )
    fig.show();

interact(bubble_chart, n=10)

ipywLayout = widgets.Layout(border='solid 2px green')
ipywLayout.display='none'
widgets.VBox([fig], layout=ipywLayout)


# In[25]:


## plotting the 10 highest prosvar från varde 1, grupperade av bedömningar (GRÖN, GUL och RÖD färger)
fig = go.FigureWidget( layout=go.Layout() )

def bubble_chart(n):
    fig = px.scatter(data1_clean.head(n), x="personnummer", y="varde2", size="varde2", color="total_bedomning",
               hover_name="personnummer", size_max=60)
    fig.update_layout(
    title=str(n) +" Highest values 2",
    xaxis_title="Patient",
    yaxis_title="Värde 2",
    width = 700
    )
    fig.show();

interact(bubble_chart, n=10)

ipywLayout = widgets.Layout(border='solid 2px green')
ipywLayout.display='none'
widgets.VBox([fig], layout=ipywLayout)


# In[26]:


import plotly.express as px

fig = px.scatter_matrix(data1_clean, dimensions=['varde1', 'varde2', 'varde3',
       'varde4', 'varde5', 'total_bedomning'], color="total_bedomning")
fig.show()


# In[27]:


### TO DO:
### Set personnummer and/or provsvarsdate as index
### Plot timeseries and table searchable by personnummer

#data1_clean.set_index("personnummer", inplace=True)

#data1_clean.head()
#data1_index[8201113179]


# In[28]:


## Resources
## Deploying the Jypter Notebook

#!pip install --upgrade pip


### Turning our Jupyter notebooks into a standalone web application using Voila Python package
# [source](https://towardsdatascience.com/creating-interactive-jupyter-notebooks-and-deployment-on-heroku-using-voila-aa1c115981ca)

#### Install voila from the command line
#```
#pip install voila
#pip install voila-material (optional)
#pip install voila-material
#```

#### After installation,  run the command in any terminal
#```
#voila patient_provsvar_anonym_dashboard_voila.ipynb 
#```




# In[29]:


#!pip install voila
#!pip install voila-material


# In[30]:


#!pip freeze


# ## [Notebook](https://github.com/dnzengou/provsvar_visu/su_banner.png)
# 
# ## Link to the analysis and other resources:
# * [Link to GitHub repo: ](https://github.com/dnzengou/provsvar_visu)
# * #voila patient_provsvar_anonym_dashboard_voila.ipynb --strip_sources=False
# * [Link to Author's Youtube: ](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ?view_as=subscriber)
# 

# In[ ]:




