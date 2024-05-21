# import gdown
# gdown.download("http://bit.ly/3RhoNho","ns_202104.csv",quiet=False)

import pandas as pd

ns_df=pd.read_csv("ns_202104.csv",low_memory=False)
# print(ns_df.head())

ns_book =ns_df.loc[:, "번호":"등록일자"]

# print("check")
#
# print(ns_df.columns)
# # print(ns_df.columns[0])
#
# print(type(ns_df.columns))
#
# print(ns_df.columns!="Unnamed:13")


## loc 함수에 대한 기본 개념 체크
# 일반적으로 생각하는 리스트가 아니라 아래의 리스트처럼 구분짓는 방식 불가능

new=[]

# for i,j in ns_df.colums:
#     if i!="부가 기호":
#         new.append(i)
#
# print(new)

# selected_colums =ns_df.columns != "부가기호"
# ns_book=ns_df.loc[:,selected_colums]
#
# print(ns_book.head())

# 열 삭제 drop

# ns_book =ns_df.drop(["Unnamed: 13","부가기호"],axis=1)
#
# print(ns_book.head())

# inplace 매개변수
# 이해 과정
# sort()바로 할 수 있다는 부분
ns_book.drop(["등록일자","부가기호","대출건수"],axis=1,inplace=True)

# print(ns_book.head())

# dropna 사용하기
