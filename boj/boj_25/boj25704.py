# 어떤 쿠폰을 쓸 수 있는가?
n = int(input())
p = int(input())
coupon_list = ['p', 'p-500', 'p*0.9', 'p-2000', 'p*0.75']
coupon_list = coupon_list[:(n//5 + 1)]

# 어떤 쿠폰이 최선인가?
coupon_list = list(map(eval, coupon_list))
best_p = min(coupon_list)

# 그 쿠폰을 쓰면 얼마를 내야 하는가?
if best_p < 0: print(0)
else: print(int(best_p))