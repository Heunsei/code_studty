# 평탄화

for num in range(10):
    T = int(input())
    tc = list(map(int, input().split()))
    
    for repeat in range(T):
        top = 0
        bottom = 100
        for n in range(100):
            for case in tc:
                if top < tc[n]:
                    top = tc[n]
                    top_idx = n
                if bottom > tc[n]:
                    bottom = tc[n]
                    bottom_idx = n
        tc[top_idx] -= 1
        tc[bottom_idx] += 1
        
        top = 0
        bottom = 100
        for n in range(100):
            for case in tc:
                if top < tc[n]:
                    top = tc[n]
                    top_idx = n
                if bottom > tc[n]:
                    bottom = tc[n]
                    bottom_idx = n
        
    #print(tc)    
    result = tc[top_idx] - tc[bottom_idx]
    #print(tc[top_idx])
    #print(tc[bottom_idx])
    print(f'#{num+1} {result}')