names = ['John', 'David']
ages = [16, 25]
isTeenager = [True, False]

users = list(zip(names, ages, isTeenager))
print(users)

print('User age:', dict(zip(names, ages)))