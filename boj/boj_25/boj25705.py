n = int(input())
board = input()
m = int(input())
obj = input()
ptr = n - 1
res_str = ''
res = 0
obj_ptr = 0
rot_without_find = 0

while res_str != obj:
    ptr = (ptr+1) % n
    res += 1
    rot_without_find += 1
    if board[ptr] == obj[obj_ptr]:
        res_str += board[ptr]
        obj_ptr += 1
        rot_without_find = 0
    if rot_without_find == n:
        res = -1
        break
    
print(res)