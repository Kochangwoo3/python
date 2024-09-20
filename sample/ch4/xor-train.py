from sklearn import svm, metrics

# Support Vector Classification 알고리즘을 구현한 클래스
# 지도학습 방식의 분류 알고리즘으로, 특히 비선형 분류 문제에 강력한 성능 보여줌

# 원본데이터
xor_data = [
  [0, 0, 0], 
  [0, 1, 1], 
  [1, 0, 1], 
  [1, 1, 0]
  ]
# 학습을 위해 데이터와 레이블 분리하기
data = []
label = []
for row in xor_data:
  p = row[0]
  q = row[1]
  r = row[2]
  data.append([p, q])
  label.append(r)


clf = svm.SVC()
# 데이터 학습시키기
clf.fit(data, label)

# 데이터 예측하기
pre = clf.predict(data)
# [0, 1]
print("예측결과: ", pre)

ok = 0
total = 0
# 결과 확인하기 : 정답률
for idx, answer in enumerate(label): # 정답
  p = pre[idx]
  if p == answer:
    ok += 1 # 정답맞춘 건수
  total += 1 # 전체건수

print("정답률 : " , ok, "/", total, " = ", ok/total)

# 정답률 구하기
ac_score = metrics.accuracy_score(label, pre) # (정답, 예측값)
print("metrics.accuracy_score 정답률 = ", ac_score)