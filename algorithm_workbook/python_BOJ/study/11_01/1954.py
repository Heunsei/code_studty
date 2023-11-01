# n가지 종류의 화학시약
# 용액의 양 m
# ax + b만큼 가스 발생

n = int(input())
candidate = []
for i in range(n):
    a, b = map(int , input().split())
    candidate.append((a,b))
m = int(input())

candidate.sort()


# N개의 시약들을 하나씩 올려가면서 확인하는 방법...
solution = 0
while True:
    res = [()]
    # 종료조건
    can_go = True
    if solution > m:
        break
    acc = 0
    # 남은 용액의 양
    left_solution = m - solution
    # 맨처음 시약을 비교 후보군으로 사용
    first_a, first_b = candidate[0]
    # 생성되어야 할 가스의 양
    compare = first_a * solution + first_b


    res.append(compare)
    print('========================')
    for i in range(1,n):
        compare_a, compare_b = candidate[i]
        print(f'compare a : {compare_a}')
        print(f'compare b : {compare_b}')
        # 나와야 할 가스양 보다 b가 더 크다면  break
        if compare < compare_b:
            can_go = False
            continue
        # 같은양의 가스를 만들기위해 필요한 용액의 양
        to_add_to_acc = (compare - compare_b) / compare_a
        next_gas = compare_a * to_add_to_acc + compare_b
        if to_add_to_acc % 1 == 0 and (acc+left_solution) <= m:
            acc += to_add_to_acc
            left_solution -= to_add_to_acc
            can_go = True
            res.append(next_gas)
            print(f'가스가스가스 : {compare}')
            print(f'맨처음 선택한 용액의 양 : {solution}')
            print(f'현재 더해야할 용액의 양 : {to_add_to_acc}')
            print(f'현재까지 쓴 용액의 양 : {acc+to_add_to_acc}')
        else:
            can_go = False


    print(f'남은 용액의 양 : {left_solution}')
    print('========================')

    if can_go and left_solution==0 and len(res) == 1:
        print(f'결과 : {compare}')
        break
    else:
        solution += 1
print(0)




