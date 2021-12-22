# Patient provsvar anonym resultat

![SU Image](https://static.nichehuset.dk/annoncer/jobannoncer/images/annoncoerer/logoer/2123/1322.png)


```python
from datetime import date

today = date.today()
print("Today's date:", today)
```

    Today's date: 2021-12-22
    


```python
# Create a requirements text file with all the libraries installed in your environment.
#!pip freeze
```


```python
## Save notebook as pdf
# Enter this in the command line

#!pip install -U notebook-as-pdf
#pyppeteer-install
```


```python
#!pip install seaborn
```


```python
#!pip install plotly
```


```python
#!pip install folium
```


```python
#!pip3 install openpyxl
```


```python
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
```


```python
data1 = pd.read_csv("https://raw.githubusercontent.com/dnzengou/provsvar_visu/main/assets/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")
#data1 = pd.read_csv("../assets/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")

#data1.head()
```


```python
# data cleaning

# renaming the df column names to lowercase
data1.columns = map(str.lower, data1.columns)

data1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>personnummer</th>
      <th>provsvarsdate</th>
      <th>provsvar 1</th>
      <th>värde 1</th>
      <th>bedömning 1</th>
      <th>provsvar 2</th>
      <th>värde 2</th>
      <th>bedömning 2</th>
      <th>provsvar 3</th>
      <th>värde 3</th>
      <th>bedömning 3</th>
      <th>provsvar 4</th>
      <th>värde 4</th>
      <th>bedömning 4</th>
      <th>provsvar 5</th>
      <th>värde 5</th>
      <th>bedömning 5</th>
      <th>total bedomning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8201113128</td>
      <td>22/12/2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, fritt, P-</td>
      <td>4.50</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.49</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.64</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8201113131</td>
      <td>15/12/2021</td>
      <td>T4, fritt, P-</td>
      <td>17</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>0.76</td>
      <td>GUL</td>
      <td>TSH, P-</td>
      <td>2.8</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.59</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.60</td>
      <td>GRON</td>
      <td>GUL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8201113134</td>
      <td>14/12/2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.10</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>5.1</td>
      <td>GUL</td>
      <td>ASAT, P-</td>
      <td>0.40</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.28</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8201113137</td>
      <td>13/12/2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.00</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.8</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.30</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.27</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8201113140</td>
      <td>18/12/2021</td>
      <td>T4, fritt, P-</td>
      <td>15</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.30</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.1</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.33</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.18</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
  </tbody>
</table>
</div>




```python
#print(data1.columns)
```


```python
data1.rename(columns = {'provsvar 1':'provsvar1', 'provsvar 2':'provsvar2', 'provsvar 3':'provsvar3', 'provsvar 4':'provsvar4', 'provsvar 5':'provsvar5', 'provsvar 6':'provsvar6', 'värde 1':'varde1', 'värde 2':'varde2', 'värde 3':'varde3', 'värde 4':'varde4', 'värde 5':'varde5',
                              'värde 6':'varde6', 'bedömning 1':'bedomning1', 'bedömning 2':'bedomning2', 'bedömning 3':'bedomning3', 'bedömning 4':'bedomning4', 'bedömning 5':'bedomning5', 'total bedomning':'total_bedomning'}, inplace = True)
#df1 = data1.rename(columns = {'total bedomning':'total_bedomning'}, inplace = True)

```


```python
# total number of confirmed, death and recovered cases
data1_total = int(data1['total_bedomning'].count())

#data1_total
```


```python
# counting unique values
unique_values = len(pd.unique(data1['total_bedomning']))
  
#print("No.of.unique values :", unique_values)
```


```python
data1_mean_varde1 = int(data1['varde1'].mean())

#data1_mean_varde1
```


```python
data1_mean_varde2 = int(data1['varde2'].mean())

#data1_mean_varde2
```


```python
data1_mean_varde3 = int(data1['varde3'].mean())

#data1_mean_varde3
```


```python
data1_mean_varde4 = int(data1['varde4'].mean())

#data1_mean_varde4
```


```python
data1_mean_varde5 = int(data1['varde5'].mean())

#data1_mean_varde5
```


```python
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
```


<div style = 'background-color: darkblue; padding: 30px '><span style='color: #fff; font-size:30px;'> Total bedömning: 40</span><span style='color: red; font-size:30px;margin-left:20px;'> medelvärde 1: 14</span><span style='color: lightgreen; font-size:30px; margin-left:20px;'> medelvärde 2: 1</span><span style='color: lightblue; font-size:30px; margin-left:20px;'> medelvärde 3: 2</span><span style='color: lightyellow; font-size:30px; margin-left:20px;'> medelvärde 4: 0</span><span style='color: lightpink; font-size:30px; margin-left:20px;'> medelvärde 5: 0</span></div>


# Patient provsvar och bedömningar


```python
## Data cleaninng

data1_clean = data1.dropna()
#data1_clean.head()

```

#### Dataset subset by color values (GRON, GUL, RÖD)
#### with conditional formatting


```python
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

```


```python
def show_latest_cases(n):
    n = int(n)
    return data1_clean.sort_values('provsvarsdate', ascending= False).head(n).style.applymap(colored_background)

interact(show_latest_cases, n='10')

ipywLayout = widgets.Layout(border='solid 2px green')
ipywLayout.display='none' # uncomment this, run cell again - then the graph/figure disappears
#widgets.VBox([fig], layout=ipywLayout)
```


    interactive(children=(Text(value='10', description='n'), Output()), _dom_classes=('widget-interact',))


## Slide to check for the highest 'provsvar' and 'bedomning'


```python
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
```


    interactive(children=(IntSlider(value=10, description='n', max=30, min=-10), Output()), _dom_classes=('widget-…



    VBox(children=(FigureWidget({
        'data': [], 'layout': {'template': '...'}
    }),), layout=Layout(border='solid …



```python
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
```


    interactive(children=(IntSlider(value=10, description='n', max=30, min=-10), Output()), _dom_classes=('widget-…



    VBox(children=(FigureWidget({
        'data': [], 'layout': {'template': '...'}
    }),), layout=Layout(border='solid …



```python
import plotly.express as px

fig = px.scatter_matrix(data1_clean, dimensions=['varde1', 'varde2', 'varde3',
       'varde4', 'varde5', 'total_bedomning'], color="total_bedomning")
fig.show()
```


<div>                            <div id="c646232e-fa3f-474d-90ef-e321b3d775ad" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("c646232e-fa3f-474d-90ef-e321b3d775ad")) {                    Plotly.newPlot(                        "c646232e-fa3f-474d-90ef-e321b3d775ad",                        [{"dimensions":[{"axis":{"matches":true},"label":"varde1","values":[13,16,16,15,12,14,13,13,12,14,12,19,16,14,14,16,19,14,17,19,16,16,16,16,16,14,15,13,14,16,13,16,15,16,13,13]},{"axis":{"matches":true},"label":"varde2","values":[4.5,1.1,1.0,1.3,0.91,1.3,1.5,3.8,1.1,1.2,1.2,3.8,0.93,3.3,4.2,1.3,0.72,1.0,3.6,3.4,1.1,0.87,1.4,0.95,1.2,0.94,1.3,1.4,0.91,1.0,0.92,0.75,1.1,1.2,1.3,1.0]},{"axis":{"matches":true},"label":"varde3","values":[1.0,5.1,1.8,1.1,3.2,0.1,2.9,0.1,4.1,5.8,3.8,0.6,0.9,2.1,1.4,1.7,2.3,1.0,2.4,2.7,0.4,6.4,2.9,1.3,1.4,0.9,1.1,1.7,1.7,1.7,3.9,2.2,1.6,1.8,2.3,2.3]},{"axis":{"matches":true},"label":"varde4","values":[0.49,0.4,0.3,0.33,0.66,0.37,0.68,0.63,0.47,0.46,0.55,0.37,0.33,0.26,0.71,0.69,0.27,0.43,0.59,0.45,0.32,0.52,0.44,0.45,0.4,0.29,0.37,0.41,0.4,0.44,0.65,0.37,0.28,0.44,0.79,0.8]},{"axis":{"matches":true},"label":"varde5","values":[0.64,0.28,0.27,0.18,0.36,0.38,0.61,0.47,0.7,0.45,0.37,0.21,0.16,0.14,0.58,0.65,0.22,0.31,0.49,0.29,0.15,0.48,0.72,0.48,0.18,0.34,0.33,0.41,0.31,0.24,0.54,0.32,0.19,0.24,0.92,0.92]},{"axis":{"matches":true},"label":"total_bedomning","values":["GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON","GRON"]}],"hovertemplate":"total_bedomning=GRON<br>%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}<extra></extra>","legendgroup":"GRON","marker":{"color":"#636efa","symbol":"circle"},"name":"GRON","showlegend":true,"type":"splom"},{"dimensions":[{"axis":{"matches":true},"label":"varde1","values":[17,14,11]},{"axis":{"matches":true},"label":"varde2","values":[0.76,1.4,1.2]},{"axis":{"matches":true},"label":"varde3","values":[2.8,1.3,1.7]},{"axis":{"matches":true},"label":"varde4","values":[0.59,0.36,0.56]},{"axis":{"matches":true},"label":"varde5","values":[0.6,0.29,0.59]},{"axis":{"matches":true},"label":"total_bedomning","values":["GUL","GUL","GUL"]}],"hovertemplate":"total_bedomning=GUL<br>%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}<extra></extra>","legendgroup":"GUL","marker":{"color":"#EF553B","symbol":"circle"},"name":"GUL","showlegend":true,"type":"splom"},{"dimensions":[{"axis":{"matches":true},"label":"varde1","values":[18]},{"axis":{"matches":true},"label":"varde2","values":[1.0]},{"axis":{"matches":true},"label":"varde3","values":[0.3]},{"axis":{"matches":true},"label":"varde4","values":[0.39]},{"axis":{"matches":true},"label":"varde5","values":[0.34]},{"axis":{"matches":true},"label":"total_bedomning","values":["R\u00d6D"]}],"hovertemplate":"total_bedomning=R\u00d6D<br>%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}<extra></extra>","legendgroup":"R\u00d6D","marker":{"color":"#00cc96","symbol":"circle"},"name":"R\u00d6D","showlegend":true,"type":"splom"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"legend":{"title":{"text":"total_bedomning"},"tracegroupgap":0},"margin":{"t":60},"dragmode":"select"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('c646232e-fa3f-474d-90ef-e321b3d775ad');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
### TO DO:
### Set personnummer and/or provsvarsdate as index
### Plot timeseries and table searchable by personnummer

#data1_clean.set_index("personnummer", inplace=True)

#data1_clean.head()
#data1_index[8201113179]
```


```python
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




```


```python
#!pip install voila
#!pip install voila-material
```


```python
#!pip freeze
```

## [Notebook](https://github.com/dnzengou/provsvar_visu/su_banner.png)

## Link to the analysis and other resources:
* [Link to GitHub repo: ](https://github.com/dnzengou/provsvar_visu)
* #voila patient_provsvar_anonym_dashboard_voila.ipynb --strip_sources=False
* [Link to Author's Youtube: ](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ?view_as=subscriber)



```python

```
