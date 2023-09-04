get_string = list(input())
tmp = []
for i in get_string[::-1]:
    tmp.append(i)
#print(tmp)
if tmp == get_string:
    print('1')
else:
    print('0')