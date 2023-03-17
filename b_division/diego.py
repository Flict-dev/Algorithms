n = int(input())
diego_list = sorted(set(map(int, input().split())))
k = int(input())
k_list = list(map(int, input().split()))

for i in k_list:
    cur = 0
    low, high, = (
        0,
        len(diego_list) - 1,
    )
    mid = (low + high) // 2
    while low <= high:
        mid = (low + high) // 2
        if diego_list[mid] < i:
            cur += mid - cur + 1
            low = mid + 1
        else:
            high = mid - 1
    print(cur)
