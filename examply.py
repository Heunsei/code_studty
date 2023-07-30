dict = {'first' : 1, 'second' : 2,'third' : 3,'fourth' : 4 }
dict['first'] = 55
dict.setdefault('lol', 10)
# print(dict)
dict['mySQL'] = 'what'
tmp = list(map(str,dict.keys()))
print(tmp[1][3])