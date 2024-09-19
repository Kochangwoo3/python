"""
  YAML : 사람이 읽기 쉽고 작성하기 쉬운 데이터 직렬화 언어
          컴퓨터가 이해할 수 있도록 표현하는 방법 중 하나입니다.
  사용목적 : 가독성이 좋음(들여쓰기 기반 구조), 구성(설정)파일로 활용하기 좋음
"""
import yaml
# YAML 정의하기 ---- (※1)
yaml_str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""

# YAML 분석
data = yaml.safe_load(yaml_str)

# 이름과 가격 출력
for item in data['PriceList']:
  print(item["name"], item["price"])

# # 댓글 데이터 예시
# comments:
#   - author: Alice
#     content: "This is a great article!"
#   - author: Bob
#     content: "I agree."

# # 사용자 설정 예시
# user:
#   name: John Doe
#   age: 30
#   is_active: true
#   address:
#     street: 123 Main St
#     city: Anytown
#     state: CA
#     zip: 12345