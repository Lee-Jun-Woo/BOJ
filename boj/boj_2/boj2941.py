word = input()
excepts = ['lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']
while 'dz=' in word: 
    word = word[:(word.find('dz='))] + '0' + word[(word.find('dz='))+3:]
for i in excepts:
    while i in word:
        word = word[:(word.find(i))] + '0' + word[(word.find(i))+2:]
print(len(word))