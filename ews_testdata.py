# -*- coding: utf-8 -*-
"""EWS_TestData

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-L_x_WzabjfmSXpi0XxYoKn7n2FOviZM
"""

import pandas as pd
import numpy as np

df=pd.read_excel ('/content/drive/MyDrive/Real Data.xlsx',parse_dates=['Dates'])

df.info()

df.head()

a=df.groupby("Company").count()
b=a["Dates"]
c=[]

for comp in df["Company"]:
    if(b[comp]==285):
        vars()['comp_'+str(comp)]=df[df['Company'] == comp]
        #vars()['comp_'+str(comp)]=df.groupby("Company").get_group(comp, obj=None)

comp_0

comp_1



adf=pd.concat([comp_0,comp_1,comp_2,comp_23,comp_28,comp_45,comp_52],ignore_index=True, sort=False)

adf

!pip install fbprophet

from fbprophet import Prophet

columns=df.columns
df_final=adf[columns].rename({'Dates':'ds','Y':'y'},axis='columns')

df_final.head()

!pip install utils









Compy=df_final.groupby('Company')

Compy.head()

for company in Compy.groups:
    group = Compy.get_group(company)
    train=group[(group['ds'] >= '2016-10-24' ) & (group['ds'] <= '2020-08-17' )]
    test=group[(group['ds'] > '2020-08-17' )]

train.shape

test.shape

target=pd.DataFrame()



for company in Compy.groups:
    group = Compy.get_group(company)
    
    m = Prophet(seasonality_mode='multiplicative',interval_width=0.90)
    #m.add_regressor('X1',standardize=False)
    '''m.add_regressor('X2',standardize=False,mode='multiplicative')
    m.add_regressor('X3',standardize=False,mode='multiplicative')
    m.add_regressor('X4',standardize=False,mode='multiplicative')
    m.add_regressor('X5',standardize=False,mode='multiplicative')
    m.add_regressor('X6',standardize=False,mode='multiplicative')'''
    m.fit(group)
    future = m.make_future_dataframe(periods=16, freq = 'W', include_history ='True')

    forecast = m.predict(future)
    m.plot(forecast)
    forecast = forecast.rename(columns={'yhat': 'yhat_'+str(company)})
    target = pd.merge(target, forecast.set_index('ds'), how='outer', left_index=True, right_index=True)



target = target[['yhat_' + str(company) for company in Compy.groups.keys()]]

target

pd.concat([df_final.set_index('ds').query("Company==0")['y'],target['yhat_0']],axis=1).plot()

