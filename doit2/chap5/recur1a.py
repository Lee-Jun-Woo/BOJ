# 비재귀적 재귀 함수 구현하기(꼬리 재귀를 제거)

def recur(n: int) -> None:
    """꼬리 재귀를 제거한 recur() 함수"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2

x = int(input('정숫값을 입력하세요.: '))

recur(x)