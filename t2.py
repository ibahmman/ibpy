username = input('Enter username :')
password = input('Enter password :')

if username == 'admin' and password == '1234':
    print('vared shodid !')
    num_1 = int(input('Enter num 1 :'))
    num_2 = int(input('Enter num 2 :'))
    num_3 = int(input('Enter num 3 :'))
    if num_1 % 2 == 0 and num_2 % 2 == 0 and num_3 % 2 == 0:
        print('har 3 adad zoj hastand !')
    elif num_1 % 2 == 0 or num_2 % 2 == 0 or num_3 % 2 == 0:
        print('had aqal 1 adad zoj ast !')
    else:
        print('har 3 adad fard hastand !')
else:
    print('username ya password eshtbah ast !')