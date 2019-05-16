lis = ['afee', 3, 44, '2', 'f134', '-344', -212, 3, 54, 26]
ref = ''
for i in range(0, len(lis)):
    if i%2 == 0:
        ref += str(lis[i]) + ' '
print(ref)
