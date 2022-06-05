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


whr_2019 = pd.read_csv("./archive/2019.csv")
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")

print(plt.style.available)# it shows all the plot styles
#plt.style.use('fivethirtyeight') here you choose your style
plt.savefig('plot.png')#how to save the plot to image
#plt.show()
