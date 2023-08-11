import pandas as pd 
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from datetime import datetime


## 매일 파일을 가져와야 함
## 데이터 csv파일로 저장하기 
daily_all_commu = pd.read_csv("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\community_content\\230803_daily_commu.csv", encoding='utf-8-sig')
daily_all_commu = daily_all_commu.loc[:, "content"].to_list()




# 불용어 지정. 많으면 많을 수록 좋을 듯.. 
stopwords = ['-', 'jpg', 'ㅋ', '[ㅇㅎ]', "gif", '스압', 'ㅇㅎ', 'ㄷ', "ㅎ", ';', 'twt', 'blind', 'pann', 'gisa', '★', '☆', 'ㅠ', 'ㅜ', "manhwa", "mp4", "후방", "레전드", "주의", "JPG", 'webp', "boja"]
# 불용어가 제거된 데이터를 저장할 새로운 리스트
filtered_list = []
for item in daily_all_commu:
    for stopword in stopwords:
        item = item.replace(stopword, '')
    filtered_list.append(item.strip())
# 총 데이터 갯수 확인
print(len(filtered_list))

# vectorizer와 lda모델 학습
vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
X = vectorizer.fit_transform(filtered_list)
#LDA 모델 학습
num_topics = 6 # 원하는 토픽의 수 설정
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
lda_model.fit(X)
# 중복제거하지 않은 토픽들 list 
keyword_li= []
# display 토픽 보여주기 
def display_topic_words(lda_model, feature_names, num_top_words):
    for topic_idx, topic in enumerate(lda_model.components_):

        # Topic별로 1000개의 단어들(features)중에서 높은 값 순으로 정렬 후 index를 반환해줌
        # argsort()는 default가 오름차순(1, 2, 3,..) 그래서[::,-1]로 내림차순으로 바꾸기
        topic_word_idx = topic.argsort()[::-1]
        top_idx = topic_word_idx[:num_top_words]
        
        # CountVectorizer 함수 할당시킨 객체에 get_feature_names()로 벡터화시킨 feature(단어들) 볼 수 있음.
        # 이 벡터화시킨 단어들(features)은 숫자-알파벳순으로 정렬되며, 단어들 순서는 fit_transform시키고 난 이후에도 동일! 
        # "문자열".join함수로 특정 문자열 사이에 끼고 문자열 합쳐줄 수 있음
        feature_concat = " ".join([str(feature_names[i])+""for i in top_idx[:2]])
        keyword_li.append(feature_concat)

feature_names = vectorizer.get_feature_names_out()
display_topic_words(lda_model, feature_names, 15)

# 중복제거한 키워드들 담을 = keyword_list
keyword_list = []
for lii in keyword_li: 
    uniq = list(lii.split(" "))
    senten = " ".join(q for q in list(dict.fromkeys(uniq)))
    keyword_list.append(senten)
print(keyword_list)



keyword_df = pd.DataFrame(keyword_list, columns= [datetime.today().strftime("%Y%m%d")])

if not os.path.exists("keyword.csv"):
    keyword_df.to_csv("keyword.csv", index=False, encoding='utf-8-sig')
else:
    exist_df = pd.read_csv("keyword.csv", encoding="utf-8-sig")
    updated_df = pd.concat([exist_df, keyword_df], axis = 1)
    # 수정된 DataFrame을 CSV 파일에 저장 (mode='a'로 기존 파일에 추가)
    updated_df.to_csv("keyword.csv", encoding="utf-8-sig", index=False)


# pickle로 저장 
with open('lda_model.pkl', 'wb') as f:
    pickle.dump(lda_model, f)