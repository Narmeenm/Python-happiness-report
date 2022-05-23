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
    return render_template('landing.html')



if __name__ == '__main__':
    app.run(debug=True)
