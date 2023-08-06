arr = [[None]*15 for _ in range(5)]
word = [input() for _ in range(5)]
#print(word[0])
#print(len(word[0]))

for i in range(5):
    for j in range(len(word[i])):
        arr[i][j] = word[i][j]

# for j in range(15):
#     for i in range(5):
#         if arr[i][j] != None:
#             print(arr[i][j], end='')

di = 1
dj = 0
for i in range(15):
