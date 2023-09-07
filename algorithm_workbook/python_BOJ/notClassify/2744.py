N = input()
for i in N:
    if i.isupper():
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
