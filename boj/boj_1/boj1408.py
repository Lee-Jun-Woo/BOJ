now_h, now_m, now_s = map(int, input().split(':'))
start_h, start_m, start_s = map(int, input().split(':'))
diff_h, diff_m, diff_s = start_h-now_h, start_m-now_m, start_s-now_s
if diff_s < 0:
    diff_m -= 1
    diff_s += 60
if diff_m < 0:
    diff_h -= 1
    diff_m += 60
if diff_h < 0:
    diff_h += 24
print('%02d:%02d:%02d' % (diff_h, diff_m, diff_s))