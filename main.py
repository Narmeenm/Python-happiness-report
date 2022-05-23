from flask import *
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from sqlalchemy import create_engine
from  matplotlib.ticker import FuncFormatter

app = Flask(__name__)

@app.route('/')
def index():
    whr_2019 = pd.read_csv("./archive/2019.csv")
    whr_2018 = pd.read_csv("./archive/2018.csv")
    whr_2017 = pd.read_csv("./archive/2017.csv")
    whr_2016 = pd.read_csv("./archive/2016.csv")
    whr_2015 = pd.read_csv("./archive/2015.csv")
    whr_2017 = whr_2017.rename(columns= {'Family':'Social support', 'Happiness.Rank':'Happiness Rank', 'Happiness.Score':'Happiness Score','Economy..GDP.per.Capita.':'Economy (GDP per Capita)', 'Health..Life.Expectancy.':'Health (Life Expectancy)', 'Trust..Government.Corruption.':'Trust (Government Corruption)', 'Dystopia.Residual':'Dystopia Residual'})
    whr_2018 = whr_2018.rename(columns = {'Overall rank':'Happiness Rank','Country or region':'Country', 'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom', 'Healthy life expectancy':'Health (Life Expectancy)', 'Perceptions of corruption':'Trust (Government Corruption)'})
    whr_2019 = whr_2019.rename(columns = {'Overall rank':'Happiness Rank','Score':'Happiness Score','Country or region':'Country', 'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom', 'Healthy life expectancy':'Health (Life Expectancy)', 'Perceptions of corruption':'Trust (Government Corruption)'})
    table_2015 = whr_2015.head(10).reset_index(drop=True)
    return render_template('landing.html',table=table_2015.to_html())



if __name__ == '__main__':
    app.run(debug=True)
