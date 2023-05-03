import chardet
import pandas as pd
# with open("서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv", encoding="EUC-KR") as f:
#
#     print(f.readline())
#     print(f.readline())


# df=pd.read_csv("서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv",encoding="EUC-KR",low_memory=False)
# # df=pd.read_csv("서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv",encoding="EUC-KR",dtype={'ISBN':str, "세트 ISBN":str, "주제분류번호":str})
# """위의 두 문장의 차이는 dtype 지정시에는 좀 더 적은 메모리 사용 가능 """

with open("practice_library.csv","rt", encoding="UTF-8") as f:
    for i in range(3):
        print(f.readline(),end="")

