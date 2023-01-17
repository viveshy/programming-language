avatars = ['Ram', 'Krishna', 'Matsya']

# loop through whole list
print('Looping entire list...')
for avatar in avatars:
    print(avatar)

# loop through some portion of list
print('Looping through sliced list')
for avatar in avatars[0:2]:
    print(avatar)

# break and continue
for avatar in avatars:
    if avatar == 'Krishna':
        print('Mahabharat!')
        break
    else:
        continue