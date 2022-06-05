from flask import *
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from sqlalchemy import create_engine
from  matplotlib.ticker import FuncFormatter
from io import BytesIO
import base64


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
    whr_2015 = whr_2015.rename(columns = {'Family':'Social support'})
    whr_2016 = whr_2016.rename(columns = {'Family':'Social support'})
    table_2015 = whr_2015.head(10).reset_index(drop=True)



    #here the plot of 6 figures of the correlation of each factor with the six factores.
    f, axs = plt.subplots(3,2, figsize = (15,15))
    #f.set_facecolor('xkcd:salmon') #to change the background of the figure that containe all the graphs
    sns.regplot(x="Economy (GDP per Capita)", y="Happiness Score", data=whr_2019, ax = axs[0, 0])
    sns.regplot(x="Social support", y="Happiness Score", data=whr_2019, ax = axs[0, 1])
    sns.regplot(x="Health (Life Expectancy)", y="Happiness Score", data=whr_2019, ax = axs[1, 0])
    sns.regplot(x="Freedom", y="Happiness Score", data=whr_2019, ax = axs[1, 1])
    sns.regplot(x="Generosity", y="Happiness Score", data=whr_2019, ax = axs[2, 0])
    sns.regplot(x="Trust (Government Corruption)", y="Happiness Score", data=whr_2019, ax = axs[2, 1])
    img = BytesIO()
    plt.savefig(img, format='png')# save the image in memory using BytesIO
    plt.close()
    img.seek(0)#rewind to beginning of file
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')# load the bytes in the context as base64

    fig, axss = plt.subplots(3,2, figsize = (15,15))
    sns.regplot(x="Economy (GDP per Capita)", y="Happiness Score", data=whr_2015, ax = axss[0, 0])
    sns.regplot(x="Social support", y="Happiness Score", data=whr_2015, ax = axss[0, 1])
    sns.regplot(x="Health (Life Expectancy)", y="Happiness Score", data=whr_2015, ax = axss[1, 0])
    sns.regplot(x="Freedom", y="Happiness Score", data=whr_2015, ax = axss[1, 1])
    sns.regplot(x="Generosity", y="Happiness Score", data=whr_2015, ax = axss[2, 0])
    sns.regplot(x="Trust (Government Corruption)", y="Happiness Score", data=whr_2015, ax = axss[2, 1])
    img1 = BytesIO()
    plt.savefig(img1, format='png')# save the image in memory using BytesIO
    plt.close()
    img1.seek(0)#rewind to beginning of file
    plot_url2 = base64.b64encode(img1.getvalue()).decode('utf8')# load the bytes in the context as base64

    return render_template('landing.html',table=table_2015.to_html(),plot_url=plot_url, plot_url2 = plot_url2)



if __name__ == '__main__':
    app.run(debug=True)
