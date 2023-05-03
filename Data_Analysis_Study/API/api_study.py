import json

d={"name": "혼자 공부하는 파이썬"}
print(d["name"])
# 파이썬 객체를 JSON 파일로 변환
d_str=json.dumps(d,ensure_ascii=False)
print(d_str)

print()
print()

# JSON 문자열을 파이썬 객체로 변환
d2=json.loads(d_str)
print("구분:", d2["name"])
print(type(d2))

#바로 변환 후 사용
d3=json.loads('{"name":"혼자 공부하는 파이썬","author":"박해선"}')
print("구분",d3["name"],d3["author"])

d4=json.loads('{"name":"혼자 공부하는 파이썬","author":["박해선","홍길동"]}')
print(d4["author"][1])

d4_str="""
[{"name":"혼자 공부하는 데이터 분석", "author":"박해선" },
{"name":"혼자 공부하는 머신러닝+딥러닝","author":"박해선"}]"""

d4=json.loads(d4_str)
print("세겹 따옴표",d4[1]["name"])

