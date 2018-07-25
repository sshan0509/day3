person={'name' : 'Nick', 'address' : 'cheonan', 'email' : 'ssh@kopo.ac.kr'}
print(person)
print(person['name'])
print(person['address'])
print(person['email'])

person['name'] = 'Jay'

print(person.items())
for key, value in person.items():
    print('\nKey \\ "' + key + '"')
    print('value \\ "' + value + '"')

#key \ 'name'
# value \ 'Nick'
