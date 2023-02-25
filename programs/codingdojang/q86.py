n = int(input())
if n == 1: print("N")
else:
    print("N" + " "*(n-2) + "N")
    for i in range(n-2):
        print("N" + " "*i + "N" + " "*(n-3-i) + "N")
    print("N" + " "*(n-2) + "N")