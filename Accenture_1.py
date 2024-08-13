str=input()


def take(str):
    if not str:
        return -1
    a=int(str[0])
    for i in range(len(str),2):
        if str[i]=='A':
            a&=int(str[i+1])
        elif str[i]=='B':
            a |=int(str[i+1])
        else:
            a^=int(str[i+1])

    return a

h=take(str)
print(h)

            