# write a commnad to find the tabble on n (how to make talbe)
n = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 11):
    m = n * i
    print(n, '*', i, '=', m)
