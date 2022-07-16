lst = []
# insert user to list
for i in range(5):
    name = input('Enter name:')
    phone = int(input('Enter number:'))
    user = (name, phone)
    lst.append(user)
print(lst)

print('che kasi hazf shavad:')
remove_name = input('Enter name:')
remove_phone = int(input('Enter phone:'))

# find and remove user
found = False
for user in lst:
    if remove_name == 'admin':
        break
    elif remove_name == user[0] and remove_phone == user[1]:
        found = True
        lst.remove(user)

if not found:
    print('not found')

# print users
for i in lst:
    print(i)
