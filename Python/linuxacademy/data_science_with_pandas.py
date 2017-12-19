#!/usr/bin/env python

import datetime as dt
import pandas as pd
import numpy as np

# Read the csv file
df = pd.read_csv("temps.csv")

#print(df.head)

df['CDT'] = df['CDT'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d'))
#print(df.head)

print(pd.pivot_table(df,index=[df['CDT'].apply(lambda x: dt.datetime.strftime(x, '%B'))], values=["Mean TemperatureF"], aggfunc=np.average))

df['Month'] = df['CDT'].apply(lambda x: dt.datetime.strftime(x,'%B'))

#print(df.head)

# not working
#print(pd.pivot_table(df,index=df['CDT'].dt.day, columns=df['Month'], values='Mean TemperatureF'))

df['Above 70'] = df['Mean TemperatureF'].apply(lambda x: 1 if x > 70 else 0)

print(pd.pivot_table(df, index=df["Month"], values=["Above 70"], aggfunc=np.sum))

print(pd.pivot_table(df, index=df["Month"], values=["Max TemperatureF"], aggfunc=np.max))
