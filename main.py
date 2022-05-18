import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from sqlalchemy import create_engine
from  matplotlib.ticker import FuncFormatter

whr_2019 = pd.read_csv("./archive/2019.csv")
whr_2018 = pd.read_csv("./archive/2018.csv")
whr_2017 = pd.read_csv("./archive/2017.csv")
whr_2016 = pd.read_csv("./archive/2016.csv")
whr_2015 = pd.read_csv("./archive/2015.csv")
#print(whr_2019.head(5))
#whr_2015.info()

print(type(whr_2015))

table_engine = create_engine('sqlite://', echo=False)
whr_2015.to_sql("Year_of_2015",con = table_engine)

sql = '''
SELECT *
FROM Year_of_2015
limit 5
''';
df_sql = pd.read_sql_query(sql,con=table_engine)


#whr_2017.info()
whr_2017 = whr_2017.rename(columns= {'Family':'Social support', 'Happiness.Rank':'Happiness Rank', 'Happiness.Score':'Happiness Score','Economy..GDP.per.Capita.':'Economy (GDP per Capita)', 'Health..Life.Expectancy.':'Health (Life Expectancy)', 'Trust..Government.Corruption.':'Trust (Government Corruption)', 'Dystopia.Residual':'Dystopia Residual'})
whr_2018 = whr_2018.rename(columns = {'Overall rank':'Happiness Rank','Country or region':'Country', 'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom', 'Healthy life expectancy':'Health (Life Expectancy)', 'Perceptions of corruption':'Trust (Government Corruption)'})
whr_2019 = whr_2019.rename(columns = {'Overall rank':'Happiness Rank','Score':'Happiness Score','Country or region':'Country', 'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom', 'Healthy life expectancy':'Health (Life Expectancy)', 'Perceptions of corruption':'Trust (Government Corruption)'})


whr_2019.info()
f, axs = plt.subplots(3,2, figsize = (15,15))
sns.regplot(x="Economy (GDP per Capita)", y="Happiness Score", data=whr_2019, ax = axs[0, 0])
sns.regplot(x="Social support", y="Happiness Score", data=whr_2019, ax = axs[0, 1])
sns.regplot(x="Health (Life Expectancy)", y="Happiness Score", data=whr_2019, ax = axs[1, 0])
sns.regplot(x="Freedom", y="Happiness Score", data=whr_2019, ax = axs[1, 1])
sns.regplot(x="Generosity", y="Happiness Score", data=whr_2019, ax = axs[2, 0])
sns.regplot(x="Trust (Government Corruption)", y="Happiness Score", data=whr_2019, ax = axs[2, 1])


plt.show()
