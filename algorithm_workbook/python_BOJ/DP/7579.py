# 앱
# 어플리케이션의 수 N, 필요한 메모리 용량 M
N, M = map(int, input().split())
# 어플리케이션이 차지하는 메모리의 용량
memory = list(map(int, input().split()))
# 비활성화 후 다시 활성화 하는데 필요한 cost
cost = list(map(int, input().split()))
# cost 를 가장 작게 선택하면서 memory 의 합을 M으로


ans = []
def get_memory(mem, app_number, acc_cost):
    if ans and acc_cost > min(ans):
        return
    if mem > M:
        return
    if mem == M:
        ans.append(acc_cost)
        return
    if app_number == N:
        return
    else:
        get_memory(mem, app_number+1, acc_cost)
        get_memory(mem+ memory[app_number], app_number+1, acc_cost + cost[app_number])



get_memory(0,0,0)
print(min(ans))
