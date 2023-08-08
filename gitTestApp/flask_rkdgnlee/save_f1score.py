import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, log_loss


# 이진 분류 문제를 위한 샘플 데이터 생성
X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)


# 데이터를 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)


# 테스트 데이터에 대한 예측 확률 계산
y_pred_proba = model.predict_proba(X_test)


# 예측 확률을 이진 예측 결과로 변환
y_pred = np.argmax(y_pred_proba, axis=1)


# 정확도, F1 스코어 및 log loss 계산
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
logloss = log_loss(y_test, y_pred_proba)


print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("Log Loss:", logloss)