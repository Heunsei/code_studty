N = int(input())
arr = list(map(int, input().split()))
max_money = int(input())

lo = 0
hi = max(arr)
mid = (lo + hi) // 2
ans = 0


def is_possible(mid):
    return sum(min(r, mid) for r in arr) <= max_money


while lo <= hi:
    print(f' lo : {lo}, mid : {mid}, hi : {hi}. ans : {ans}')
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)
