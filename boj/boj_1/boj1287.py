value = input()
res_value = ''
check_value = ''
valids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')']

if value.count('()'): res_value += 'ROCK'
for sign in value:
    if sign in valids:
        res_value += sign
        check_value += sign
    elif sign == '/':
        res_value += '//'
        check_value += '&'
    else:
        res_value += sign
        check_value += '&'

try:
    eval(check_value)
    print(eval(res_value))
except:
    print('ROCK')