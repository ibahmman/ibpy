n1 = float(input('Enter number 1:'))
op = input('Enter op:')
n2 = float(input('Enter number 2:'))
name = input('Enter name:')

if op == '//':
    n = n1 // n2
    print(name * int(n))
elif op == '*':
    n = n1 * n2
    print(name * int(n))
elif op == '-':
    n = n1 - n2
    print(name * int(n))
elif op == '+':
    n = n1 + n2
    print(name * int(n))
else:
    print('op : //, *, -, +')
