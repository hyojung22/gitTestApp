import pandas as pd



# df1 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train.csv')
# df2 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train1.csv')
# df3 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train2.csv')
# df4 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train3.csv')
# df5 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train4.csv')
# df6 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train5.csv')
# df7 = pd.read_csv('news_training\\news_train_data\\preprocessing_news_train6.csv')


# df8 = pd.concat([df1, df2, df3, df4, df5, df6, df7])



# #print(df8.iloc[:,0])
# df8.rename(columns={df8.columns[0]: 'index'}, inplace=True)

# df_unique = df8.drop_duplicates(subset=['content'])

# # 중복 제거된 데이터프레임 출력
# print(df_unique)
# df_unique_content = df_unique.drop_duplicates(subset=['content'])
# df_unique_content.to_csv('pretrain_news_train.csv')

df9 = pd.read_csv('pretrain_news_train1.CSV', encoding='cp949')


df9.to_csv('pretrain_news_train2.csv', index=False, encoding='utf-8')


