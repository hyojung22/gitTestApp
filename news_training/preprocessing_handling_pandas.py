#pandas
import pandas as pd



df_news = pd.read_csv("dummy.csv")
#df_news['label'] = 0
print(df_news[['content','label']])

