def is_hansu(n: int) -> bool:
    if n < 100: return True
    elif (n//100 - n//10%10) == (n//10%10 - n%10): return True
    else: return False
N = int(input())
print(len(tuple(filter(is_hansu, range(1, N+1)))))