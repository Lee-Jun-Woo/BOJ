# 테일러 급수로 삼각함수를 구함

def factorial(x: int) -> int:
    if x:
        return x * factorial(x - 1)
    else:
        return 1

def sin(x: float, accuracy: int) -> float:
    result = 0
    for n in range(accuracy):
        result += (((-1)**n) * x**(2*n+1)) / factorial(2*n + 1)
    return result

def cos(x: float, accuracy: int) -> float:
    result = 0
    for n in range(accuracy):
        result += (((-1)**n) * x**(2*n)) / factorial(2*n)
    return result

def tan(x: float, accuracy: int) -> float:
    return  sin(x, accuracy) / cos(x, accuracy)

if __name__ == '__main__':
    accuracy_num = int(input('정확도를 입력하세요: '))
    while True:
        func = input('구할 함수를 입력하세요: ')
        val = float(input('값을 입력하세요: '))
        print(eval(f'{func}({val}, {accuracy_num})'))
        if input('계속하시겠습니까? (y/n): ') == 'n':
            break