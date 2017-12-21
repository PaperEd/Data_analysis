def sosu(x):
    cnt = 0
    for i in x:
        if i == 2:
            cnt += 1
            continue
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                cnt += 1
    return cnt


input()
print(sosu(list(map(int, input().split(' ')))))