n=int(input())
c='R'
dis=10
x,y=0,0
for i in range(n):
    if c=='R':
        x+=dis
        c='U'
        dis+=10
    elif c=='U':
        y=y+dis
        c='L'
        dis+=10
    elif c=='L':
        x-=dis
        c='D'
        dis+=10
    elif c=='D':
        y-=dis
        c='A'
        dis+=10
    elif c=='A':
        x+=dis
        c='R'
        dis+=10
print(x,y)
