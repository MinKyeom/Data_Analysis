# import gdown
# gdown.download("http://bit.ly/3RhoNho","ns_202104.csv",quiet=False)

import pandas as pd

ns_df=pd.read_csv("ns_202104.csv",low_memory=False)
print(ns_df.head())

ns_book =ns_df.loc[:, "번호":"등록일자"]

print("check")

print(ns_df.columns)
# print(ns_df.columns[0])

print(type(ns_df.columns))

print(ns_df.columns!="Unnamed:13")


## loc 함수에 대한 기본 개념 체크 
# 일반적으로 생각하는 리스트가 아니라 아래의 리스트처럼 구분짓는 방식 불가능
new=[]

# for i,j in ns_df.colums:
#     if i!="부가 기호":
#         new.append(i)
#
# print(new)