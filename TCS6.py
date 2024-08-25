from collections import Counter
a=input()
b=Counter(a)

if b['#']==b['*']:
    print('0')
elif b['#']>b['*']:
    print('negative integer')
else:
    print('positive integer')