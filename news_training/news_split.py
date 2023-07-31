#여기에 크롤링 csv 데이터를 넣어 train_x와 train_y로 나눈다
#pandas
import pandas as pd

#data_split
from sklearn.model_selection import train_test_split


#import csv

df_news = pd.read_csv("dummy.csv")

df_x_data = df_news['content']
df_y_data = df_news['label']

#create_train_data(df['content'], df['label'])

df_x_train, df_x_test, df_y_train, df_y_test = train_test_split(df_x_data, df_y_data, test_size=0.3, random_state=777, stratify=df_y_data)

#news_train.csv, news_test.csv 

df_train = pd.concat([df_x_train, df_y_train], axis=1) 
df_test = pd.concat([df_x_test, df_y_test], axis=1)

df_train.to_csv('news_train.csv')
df_test.to_csv('news_test.csv')

#export_csv
