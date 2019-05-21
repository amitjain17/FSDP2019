# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:00:40 2019

@author: NITS
"""

import pandas as pd

df = pd.read_csv("training_titanic.csv")


print(" Died {}".format(df['Survived'].value_counts()[0]),"\n","Survive {}".format(df['Survived'].value_counts()[1]))
print(" Died Percentage {}".format(df['Survived'].value_counts(normalize='True')[0]),"\n","Survive Percentage {}".format(df['Survived'].value_counts(normalize='True')[1]))

df1 =df["Survived"][(df['Sex'] == 'male')].value_counts()

print(" Man Survived {}".format(df1[1]),"\n","Man Died {}".format(df1[0]))
df1 =df["Survived"][(df['Sex'] == 'female')].value_counts()
print(" female Survived {}".format(df1[1]),"\n","female Died {}".format(df1[0]))

df['Age'] = df['Age'].fillna(int(df['Age'].mean()))
df["Age_bin"] = df['Age'].map(lambda x: 1 if x>18 else 0)
print(" child : {}".format(df['Age_bin'].value_counts()[0]),"\n","Person :{}".format(df['Age_bin'].value_counts()[1]))