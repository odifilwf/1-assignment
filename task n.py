n = int(input())

mins = n * 45 + (n // 2) * 5 + ((n-1)//2 * 15)

h = 9 + mins // 60
m = mins % 60
print(h,m)