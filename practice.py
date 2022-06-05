from flask import *
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


table_engine = create_engine('sqlite://', echo=False)
whr_2015.to_sql("Year_of_2015",con = table_engine)

sql = '''
SELECT *
FROM Year_of_2015
limit 5
''';
df_sql = pd.read_sql_query(sql,con=table_engine)



whr_2017 = whr_2017.rename(columns= {'Family':'Social support', 'Happiness.Rank':'Happiness Rank', 'Happiness.Score':'Happiness Score','Economy..GDP.per.Capita.':'Economy (GDP per Capita)', 'Health..Life.Expectancy.':'Health (Life Expectancy)', 'Trust..Government.Corruption.':'Trust (Government Corruption)', 'Dystopia.Residual':'Dystopia Residual'})
whr_2018 = whr_2018.rename(columns = {'Overall rank':'Happiness Rank','Country or region':'Country', 'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom', 'Healthy life expectancy':'Health (Life Expectancy)', 'Perceptions of corruption':'Trust (Government Corruption)'})
whr_2019 = whr_2019.rename(columns = {'Overall rank':'Happiness Rank','Score':'Happiness Score','Country or region':'Country', 'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom', 'Healthy life expectancy':'Health (Life Expectancy)', 'Perceptions of corruption':'Trust (Government Corruption)'})


#whr_2019.info()
#f, axs = plt.subplots(3,2, figsize = (15,15))
#sns.regplot(x="Economy (GDP per Capita)", y="Happiness Score", data=whr_2019, ax = axs[0, 0])
#sns.regplot(x="Social support", y="Happiness Score", data=whr_2019, ax = axs[0, 1])
#sns.regplot(x="Health (Life Expectancy)", y="Happiness Score", data=whr_2019, ax = axs[1, 0])
#sns.regplot(x="Freedom", y="Happiness Score", data=whr_2019, ax = axs[1, 1])
#sns.regplot(x="Generosity", y="Happiness Score", data=whr_2019, ax = axs[2, 0])
#sns.regplot(x="Trust (Government Corruption)", y="Happiness Score", data=whr_2019, ax = axs[2, 1])
#plt.show()



#plt.figure(figsize=(12,10), dpi= 80)
#sns.heatmap(whr_2019.corr(), xticklabels=whr_2019.corr().columns, yticklabels=whr_2019.corr().columns, cmap='RdYlGn', center=0, annot=True)
#plt.title('Correlogram of World Happiness Score in 2019', fontsize=22)
#plt.xticks(fontsize=12)
#plt.yticks(fontsize=12)
#plt.show()


#How did country ranks or scores change between the 2015 and 2019 reports?
# first see in each year which country has the highest Happiness score?
# to choose the top 7 contries
#merge the five years to one file that x = years , y = Happiness score and we have 7 axes in one figure.


whr_2015.sort_values("Happiness Score", axis = 0, ascending = False,inplace = True, na_position ='last')
head_of_2015=whr_2015.head(7)
#country_top7_name = head_of_2015.loc[:,'Country':'Happiness Score'] #how to get specific column value in pandas
df_new = head_of_2015[['Country','Happiness Score']]
df_new.rename(columns = {'Happiness Score':'Happiness Score 2015'}, inplace = True)
# Import pandas package

whr_2016.sort_values("Happiness Score", axis = 0, ascending = False,inplace = True, na_position ='last')
head_of_2016=whr_2016.head(7)
df_new_2016 = head_of_2016[['Country','Happiness Score']]
df_new_2016.rename(columns = {'Happiness Score':'Happiness Score 2016'}, inplace = True)
print(df_new)
print(df_new_2016)
whr_2017.sort_values("Happiness Score", axis = 0, ascending = False,inplace = True, na_position ='last')
head_of_2017=whr_2017.head(7)
df_new_2017 = head_of_2017[['Country','Happiness Score']]
print(df_new_2017)
merge_1516 = pd.merge(df_new,df_new_2016)
merge_2017 = pd.merge(merge_1516,df_new_2017)
print(merge_2017)

Xvalue = ['2015','2016','2017']

Switzerland =merge_2017.iloc[0]
print(type(Switzerland))

Yvalue = []
Yvalue.append(Switzerland[1])
Yvalue.append(Switzerland[2])
Yvalue.append(Switzerland[3])
print(Yvalue)

plt.plot(Xvalue, Yvalue)
plt.xlabel('years')
plt.ylabel('Happiness Score')
plt.show()

merge_2017_2 = whr_2017[(whr_2017['Country'] == 'Finland') | (whr_2017['Country'] == 'Denmark') | (whr_2017['Country'] == 'Norway')| (whr_2017['Country'] == 'Switzerland')| (whr_2017['Country'] == 'Iceland')| (whr_2017['Country'] == 'Netherlands')| (whr_2017['Country'] == 'Canada')]
merge_2017_2.loc[:,"Year"] = [2017, 2017, 2017, 2017, 2017, 2017, 2017]

print(merge_2017_2)
# below we create x & Y via lot
#xValues = df_new['Country'].to_numpy()
#yValues = df_new['Happiness Score'].to_numpy()
#plt.plot(xValues, yValues)
#plt.xlabel('Country')
#plt.ylabel('Happiness Score')
#plt.show()
